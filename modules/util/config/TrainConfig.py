from typing import Any

from modules.util.ModelNames import ModelNames
from modules.util.ModelWeightDtypes import ModelWeightDtypes
from modules.util.enum.AlignPropLoss import AlignPropLoss
from modules.util.enum.AttentionMechanism import AttentionMechanism
from modules.util.enum.DataType import DataType
from modules.util.enum.EMAMode import EMAMode
from modules.util.enum.ImageFormat import ImageFormat
from modules.util.enum.LearningRateScaler import LearningRateScaler
from modules.util.enum.LearningRateScheduler import LearningRateScheduler
from modules.util.enum.LossScaler import LossScaler
from modules.util.enum.ModelFormat import ModelFormat
from modules.util.enum.ModelType import ModelType
from modules.util.enum.Optimizer import Optimizer
from modules.util.enum.TimeUnit import TimeUnit
from modules.util.enum.TrainingMethod import TrainingMethod
from modules.util.config.BaseConfig import BaseConfig


class TrainConfig(BaseConfig):
    training_method: TrainingMethod
    model_type: ModelType
    debug_mode: bool
    debug_dir: str
    workspace_dir: str
    cache_dir: str
    tensorboard: bool
    tensorboard_expose: bool
    continue_last_backup: bool

    # model settings
    base_model_name: str
    weight_dtype: DataType
    output_dtype: DataType
    output_model_format: ModelFormat
    output_model_destination: str
    gradient_checkpointing: bool

    # data settings
    concept_file_name: str
    circular_mask_generation: bool
    random_rotate_and_crop: bool
    aspect_ratio_bucketing: bool
    latent_caching: bool
    clear_cache_before_training: bool

    # training settings
    learning_rate_scheduler: LearningRateScheduler
    learning_rate: float
    learning_rate_warmup_steps: int
    learning_rate_cycles: float
    epochs: int
    batch_size: int
    gradient_accumulation_steps: int
    ema: EMAMode
    ema_decay: float
    ema_update_step_interval: int
    train_device: str
    temp_device: str
    train_dtype: DataType
    fallback_train_dtype: DataType
    only_cache: bool
    resolution: str
    attention_mechanism: AttentionMechanism
    align_prop: bool
    align_prop_probability: float
    align_prop_loss: AlignPropLoss
    align_prop_weight: float
    align_prop_steps: int
    align_prop_truncate_steps: float
    align_prop_cfg_scale: float
    mse_strength: float
    mae_strength: float
    vb_loss_strength: float
    loss_scaler: LossScaler
    learning_rate_scaler: LearningRateScaler

    # unet
    train_unet: bool
    train_unet_epochs: int
    unet_learning_rate: float
    offset_noise_weight: float
    perturbation_noise_weight: float
    rescale_noise_scheduler_to_zero_terminal_snr: bool
    force_v_prediction: bool
    force_epsilon_prediction: bool
    min_noising_strength: float
    max_noising_strength: float
    noising_weight: float
    noising_bias: float
    unet_weight_dtype: DataType

    # prior
    train_prior: bool
    train_prior_epochs: int
    prior_learning_rate: float
    prior_weight_dtype: DataType

    # text encoder
    train_text_encoder: bool
    train_text_encoder_epochs: int
    text_encoder_learning_rate: float
    text_encoder_layer_skip: int
    text_encoder_weight_dtype: DataType

    # text encoder 2
    train_text_encoder_2: bool
    train_text_encoder_2_epochs: int
    text_encoder_2_learning_rate: float
    text_encoder_2_layer_skip: int
    text_encoder_2_weight_dtype: DataType

    # vae
    vae_model_name: str
    vae_weight_dtype: DataType

    # effnet encoder
    effnet_encoder_model_name: str
    effnet_encoder_weight_dtype: DataType

    # decoder
    decoder_model_name: str
    decoder_weight_dtype: DataType

    # decoder text encoder
    decoder_text_encoder_weight_dtype: DataType

    # decoder vqgan
    decoder_vqgan_weight_dtype: DataType

    # masked training
    masked_training: bool
    unmasked_probability: float
    unmasked_weight: float
    normalize_masked_area_loss: bool

    # embedding
    embedding_model_names: list[str]
    token_count: int
    initial_embedding_text: str
    embedding_weight_dtype: DataType

    # lora
    lora_model_name: str
    lora_rank: int
    lora_alpha: float
    lora_weight_dtype: DataType

    # optimizer settings
    optimizer: Optimizer
    optimizer_weight_decay: float
    optimizer_momentum: float
    optimizer_dampening: float
    optimizer_nesterov: bool
    optimizer_eps: float
    optimizer_foreach: bool
    optimizer_fused: bool
    optimizer_min_8bit_size: int
    optimizer_percentile_clipping: int
    optimizer_block_wise: bool
    optimizer_is_paged: bool
    optimizer_lr_decay: int
    optimizer_initial_accumulator_value: int
    optimizer_alpha: float
    optimizer_centered: bool
    optimizer_max_unorm: float
    optimizer_beta2: float
    optimizer_bias_correction: bool
    optimizer_amsgrad: bool
    optimizer_adam_w_mode: bool
    optimizer_use_bias_correction: bool
    optimizer_safeguard_warmup: bool
    optimizer_beta3: float
    optimizer_decouple: bool
    optimizer_d0: float
    optimizer_d_coef: float
    optimizer_growth_rate: float
    optimizer_fsdp_in_use: bool
    optimizer_clip_threshold: float
    optimizer_decay_rate: float
    optimizer_beta1: float
    optimizer_scale_parameter: bool
    optimizer_relative_step: bool
    optimizer_warmup_init: bool
    optimizer_eps2: float
    optimizer_optim_bits: int
    optimizer_log_every: int
    optimizer_no_prox: bool
    optimizer_maximize: bool
    optimizer_capturable: bool
    optimizer_differentiable: bool
    optimizer_use_triton: bool

    # sample settings
    sample_definition_file_name: str
    sample_after: float
    sample_after_unit: TimeUnit
    sample_image_format: ImageFormat
    samples_to_tensorboard: bool
    non_ema_sampling: bool

    # backup settings
    backup_after: float
    backup_after_unit: TimeUnit
    rolling_backup: bool
    rolling_backup_count: int
    backup_before_save: bool
    save_after: float
    save_after_unit: TimeUnit

    def __init__(self, data: list[(str, Any, type, bool)]):
        super(TrainConfig, self).__init__(data)

    def weight_dtypes(self) -> ModelWeightDtypes:
        return ModelWeightDtypes(
            self.weight_dtype if self.unet_weight_dtype == DataType.NONE else self.unet_weight_dtype,
            self.weight_dtype if self.prior_weight_dtype == DataType.NONE else self.prior_weight_dtype,
            self.weight_dtype if self.text_encoder_weight_dtype == DataType.NONE else self.text_encoder_weight_dtype,
            self.weight_dtype if self.text_encoder_2_weight_dtype == DataType.NONE else self.text_encoder_2_weight_dtype,
            self.weight_dtype if self.vae_weight_dtype == DataType.NONE else self.vae_weight_dtype,
            self.weight_dtype if self.effnet_encoder_weight_dtype == DataType.NONE else self.effnet_encoder_weight_dtype,
            self.weight_dtype if self.decoder_weight_dtype == DataType.NONE else self.decoder_weight_dtype,
            self.weight_dtype if self.decoder_text_encoder_weight_dtype == DataType.NONE else self.decoder_text_encoder_weight_dtype,
            self.weight_dtype if self.decoder_vqgan_weight_dtype == DataType.NONE else self.decoder_vqgan_weight_dtype,
            self.weight_dtype if self.lora_weight_dtype == DataType.NONE else self.lora_weight_dtype,
            self.weight_dtype if self.embedding_weight_dtype == DataType.NONE else self.embedding_weight_dtype,
        )

    def model_names(self) -> ModelNames:
        return ModelNames(
            base_model=self.base_model_name,
            effnet_encoder_model=self.effnet_encoder_model_name,
            decoder_model=self.decoder_model_name,
            vae_model=self.vae_model_name,
            lora=self.lora_model_name,
            embedding=self.embedding_model_names,
        )

    @staticmethod
    def default_values() -> 'TrainConfig':
        data = []

        # name, default value, data type, nullable

        # general settings
        data.append(("training_method", TrainingMethod.FINE_TUNE, TrainingMethod, False))
        data.append(("model_type", ModelType.STABLE_DIFFUSION_15, ModelType, False))
        data.append(("debug_mode", False, bool, False))
        data.append(("debug_dir", "debug", str, False))
        data.append(("workspace_dir", "workspace/run", str, False))
        data.append(("cache_dir", "workspace-cache/run", str, False))
        data.append(("tensorboard", True, bool, False))
        data.append(("tensorboard_expose", False, bool, False))
        data.append(("continue_last_backup", False, bool, False))

        # model settings
        data.append(("base_model_name", "runwayml/stable-diffusion-v1-5", str, False))
        data.append(("weight_dtype", DataType.FLOAT_32, DataType, False))
        data.append(("output_dtype", DataType.FLOAT_32, DataType, False))
        data.append(("output_model_format", ModelFormat.SAFETENSORS, ModelFormat, False))
        data.append(("output_model_destination", "models/model.safetensors", str, False))
        data.append(("gradient_checkpointing", True, bool, False))

        # data settings
        data.append(("concept_file_name", "training_concepts/concepts.json", str, False))
        data.append(("circular_mask_generation", False, bool, False))
        data.append(("random_rotate_and_crop", False, bool, False))
        data.append(("aspect_ratio_bucketing", True, bool, False))
        data.append(("latent_caching", True, bool, False))
        data.append(("clear_cache_before_training", True, bool, False))

        # training settings
        data.append(("learning_rate_scheduler", LearningRateScheduler.CONSTANT, LearningRateScheduler, False))
        data.append(("learning_rate", 3e-6, float, False))
        data.append(("learning_rate_warmup_steps", 200, int, False))
        data.append(("learning_rate_cycles", 1, int, False))
        data.append(("epochs", 100, int, False))
        data.append(("batch_size", 1, int, False))
        data.append(("gradient_accumulation_steps", 1, int, False))
        data.append(("ema", EMAMode.OFF, EMAMode, False))
        data.append(("ema_decay", 0.999, float, False))
        data.append(("ema_update_step_interval", 5, int, False))
        data.append(("train_device", "cuda", str, False))
        data.append(("temp_device", "cpu", str, False))
        data.append(("train_dtype", DataType.FLOAT_16, DataType, False))
        data.append(("fallback_train_dtype", DataType.BFLOAT_16, DataType, False))
        data.append(("only_cache", False, bool, False))
        data.append(("resolution", "512", str, False))
        data.append(("attention_mechanism", AttentionMechanism.XFORMERS, AttentionMechanism, False))
        data.append(("align_prop", False, bool, False))
        data.append(("align_prop_probability", 0.1, float, False))
        data.append(("align_prop_loss", AlignPropLoss.AESTHETIC, AlignPropLoss, False))
        data.append(("align_prop_weight", 0.01, float, False))
        data.append(("align_prop_steps", 20, int, False))
        data.append(("align_prop_truncate_steps", 0.5, float, False))
        data.append(("align_prop_cfg_scale", 7.0, float, False))
        data.append(("mse_strength", 1.0, float, False))
        data.append(("mae_strength", 0.0, float, False))
        data.append(("vb_loss_strength", 1.0, float, False))
        data.append(("loss_scaler", LossScaler.NONE, LossScaler, False))
        data.append(("learning_rate_scaler", LearningRateScaler.NONE, LearningRateScaler, False))

        # unet
        data.append(("train_unet", True, bool, False))
        data.append(("train_unet_epochs", 10000, int, False))
        data.append(("unet_learning_rate", None, float, True))
        data.append(("offset_noise_weight", 0.0, float, False))
        data.append(("perturbation_noise_weight", 0.0, float, False))
        data.append(("rescale_noise_scheduler_to_zero_terminal_snr", False, bool, False))
        data.append(("force_v_prediction", False, bool, False))
        data.append(("force_epsilon_prediction", False, bool, False))
        data.append(("min_noising_strength", 0.0, float, False))
        data.append(("max_noising_strength", 1.0, float, False))
        data.append(("noising_weight", 0.0, float, False))
        data.append(("noising_bias", 0.5, float, False))
        data.append(("unet_weight_dtype", DataType.NONE, DataType, False))

        # prior
        data.append(("train_prior", True, bool, False))
        data.append(("train_prior_epochs", 10000, int, False))
        data.append(("prior_learning_rate", None, float, True))
        data.append(("prior_weight_dtype", DataType.NONE, DataType, False))

        # text encoder
        data.append(("train_text_encoder", True, bool, False))
        data.append(("train_text_encoder_epochs", 30, int, False))
        data.append(("text_encoder_learning_rate", None, float, True))
        data.append(("text_encoder_layer_skip", 0, int, False))
        data.append(("text_encoder_weight_dtype", DataType.NONE, DataType, False))

        # text encoder 2
        data.append(("train_text_encoder_2", True, bool, False))
        data.append(("train_text_encoder_2_epochs", 30, int, False))
        data.append(("text_encoder_2_learning_rate", None, float, True))
        data.append(("text_encoder_2_layer_skip", 0, int, False))
        data.append(("text_encoder_2_weight_dtype", DataType.NONE, DataType, False))

        # vae
        data.append(("vae_model_name", "", str, False))
        data.append(("vae_weight_dtype", DataType.FLOAT_32, DataType, False))

        # effnet encoder
        data.append(("effnet_encoder_model_name", "", str, False))
        data.append(("effnet_encoder_weight_dtype", DataType.NONE, DataType, False))

        # decoder
        data.append(("decoder_model_name", "", str, False))
        data.append(("decoder_weight_dtype", DataType.NONE, DataType, False))

        # decoder text encoder
        data.append(("decoder_text_encoder_weight_dtype", DataType.NONE, DataType, False))

        # decoder vqgan
        data.append(("decoder_vqgan_weight_dtype", DataType.NONE, DataType, False))

        # masked training
        data.append(("masked_training", False, bool, False))
        data.append(("unmasked_probability", 0.1, float, False))
        data.append(("unmasked_weight", 0.1, float, False))
        data.append(("normalize_masked_area_loss", False, bool, False))

        # embedding
        data.append(("embedding_model_names", [], list[str], False))
        data.append(("token_count", 1, int, False))
        data.append(("initial_embedding_text", "*", str, False))
        data.append(("embedding_weight_dtype", DataType.FLOAT_32, DataType, False))

        # lora
        data.append(("lora_model_name", "", str, False))
        data.append(("lora_rank", 16, int, False))
        data.append(("lora_alpha", 1.0, float, False))
        data.append(("lora_weight_dtype", DataType.FLOAT_32, DataType, False))

        # optimizer settings
        data.append(("optimizer", Optimizer.ADAMW, Optimizer, False))
        data.append(("optimizer_adam_w_mode", None, bool, True))
        data.append(("optimizer_alpha", None, float, True))
        data.append(("optimizer_amsgrad", None, bool, True))
        data.append(("optimizer_beta1", None, float, True))
        data.append(("optimizer_beta2", None, float, True))
        data.append(("optimizer_beta3", None, float, True))
        data.append(("optimizer_bias_correction", None, bool, True))
        data.append(("optimizer_block_wise", None, bool, True))
        data.append(("optimizer_capturable", None, bool, True))
        data.append(("optimizer_centered", None, bool, True))
        data.append(("optimizer_clip_threshold", None, float, True))
        data.append(("optimizer_d0", None, float, True))
        data.append(("optimizer_d_coef", None, float, True))
        data.append(("optimizer_dampening", None, float, True))
        data.append(("optimizer_decay_rate", None, float, True))
        data.append(("optimizer_decouple", None, bool, True))
        data.append(("optimizer_differentiable", None, bool, True))
        data.append(("optimizer_eps", None, float, True))
        data.append(("optimizer_eps2", None, float, True))
        data.append(("optimizer_foreach", None, bool, True))  # Disabled, because it uses too much VRAM
        data.append(("optimizer_fsdp_in_use", None, bool, True))
        data.append(("optimizer_fused", None, bool, True))
        data.append(("optimizer_growth_rate", None, float, True))
        data.append(("optimizer_initial_accumulator_value", None, int, True))
        data.append(("optimizer_is_paged", None, bool, True))
        data.append(("optimizer_log_every", None, int, True))
        data.append(("optimizer_lr_decay", None, float, True))
        data.append(("optimizer_max_unorm", None, float, True))
        data.append(("optimizer_maximize", None, bool, True))
        data.append(("optimizer_min_8bit_size", None, int, True))
        data.append(("optimizer_momentum", None, float, True))
        data.append(("optimizer_nesterov", None, bool, True))
        data.append(("optimizer_no_prox", None, bool, True))
        data.append(("optimizer_optim_bits", None, int, True))
        data.append(("optimizer_percentile_clipping", None, float, True))
        data.append(("optimizer_relative_step", None, bool, True))
        data.append(("optimizer_safeguard_warmup", None, bool, True))
        data.append(("optimizer_scale_parameter", None, bool, True))
        data.append(("optimizer_use_bias_correction", None, bool, True))
        data.append(("optimizer_use_triton", None, bool, True))
        data.append(("optimizer_warmup_init", None, bool, True))
        data.append(("optimizer_weight_decay", None, float, True))

        # sample settings
        data.append(("sample_definition_file_name", "training_samples/samples.json", str, False))
        data.append(("sample_after", 10, int, False))
        data.append(("sample_after_unit", TimeUnit.MINUTE, TimeUnit, False))
        data.append(("sample_image_format", ImageFormat.JPG, ImageFormat, False))
        data.append(("samples_to_tensorboard", True, bool, False))
        data.append(("non_ema_sampling", True, bool, False))

        # backup settings
        data.append(("backup_after", 30, int, False))
        data.append(("backup_after_unit", TimeUnit.MINUTE, TimeUnit, False))
        data.append(("rolling_backup", False, bool, False))
        data.append(("rolling_backup_count", 3, int, False))
        data.append(("backup_before_save", True, bool, False))
        data.append(("save_after", 0, int, False))
        data.append(("save_after_unit", TimeUnit.NEVER, TimeUnit, False))

        return TrainConfig(data)
