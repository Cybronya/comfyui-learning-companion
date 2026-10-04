# Pattern: SD1.5 文生图基础模式 (sd15-t2i-basic)

## 模式定义

SD/SD1.5 系列最基础的文生图（txt2img）链路，也是 ComfyUI 默认模板工作流。
全部由内置节点构成，无任何 custom_nodes 依赖。

## 特征节点组合

```
CheckpointLoaderSimple ─┬─ MODEL → KSampler
                        ├─ CLIP  → CLIPTextEncode(positive)  ─ CONDITIONING → KSampler
                        ├─ CLIP  → CLIPTextEncode(negative)  ─ CONDITIONING → KSampler
                        └─ VAE   → VAEDecode
EmptyLatentImage ─────────────────────────────── LATENT → KSampler
KSampler ── LATENT → VAEDecode ── IMAGE → SaveImage
```

识别特征：**CLIPTextEncode ×2（正/负条件）+ EmptyLatentImage + KSampler + VAEDecode + SaveImage**，
且 denoise = 1.0（从纯噪声生成，无图生图输入）。

## 与相邻模式的区分

| 模式 | 区别点 |
|---|---|
| 图生图 (i2i) | EmptyLatentImage → LoadImage + VAEEncode，denoise < 1.0 |
| 局部重绘 (inpaint) | 增加 SetLatentNoiseMask / VAEEncodeForInpaint |
| LoRA 叠加 | CheckpointLoader 与 CLIPTextEncode 之间插入 LoraLoader |
| ControlNet 控制 | 增加 ControlNetLoader + ControlNetApply(Advanced) |

## 关键参数基准（本模式典型值）

- steps: 20 / cfg: 8.0 / sampler: euler / scheduler: normal / denoise: 1.0
- 分辨率: SD1.5 原生 512×512（最高 768 系，过大易构图崩坏）
- 负面词常见起步: text, watermark

## 来源实例

- comfyui_library/workflows/sd1.5/text-to-image-workflow.png（2026-10-04 分析，7 节点）

## 学习价值

这是理解 ComfyUI 数据流类型的"教学样本"：MODEL / CLIP / VAE / CONDITIONING / LATENT / IMAGE
六种核心 link type 在一条链路里全部出现，可作为后续分析任何复杂工作流的对照基准。
