FROM condaforge/miniforge3:latest

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY environment.yml /app/environment.yml
RUN conda env create -f environment.yml && conda clean -afy

ENV PATH=/opt/conda/envs/plasmidhub/bin:$PATH

COPY . /app
RUN python -m pip install --no-cache-dir --upgrade pip && python -m pip install --no-cache-dir .

ENTRYPOINT ["plasmidhub"]
CMD ["--help"]
