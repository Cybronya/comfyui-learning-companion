# Pattern: SD1.5 LoRA 文生图模式 (sd15-t2i-lora)

## 模式定义

在 `sd15-t2i-basic` 基础链路上，于 CheckpointLoader 与 CLIPTextEncode/KSampler 之间
插入一个 LoraLoader 的单扩展模式。全部由内置节点构成，是"底模 + 风格 LoRA"的标准形态。

## 特征节点组合

```
CheckpointLoaderSimple ─┬─ MODEL → LoraLoader ─ MODEL → KSampler
                        ├─ CLIP  → LoraLoader ─ CLIP ─┬→ CLIPTextEncode(positive) → KSampler
                        │                             └→ CLIPTextEncode(negative) → KSampler
                        └─ VAE ──────────────────────────────→ VAEDecode   ← 不经 LoRA，直连
EmptyLatentImage ──────────────────────────────────────────── LATENT → KSampler
KSampler ── LATENT → VAEDecode ── IMAGE → SaveImage
```

识别特征：**t2i 基础七件套 + 恰好 1 个 LoraLoader**，且 LoraLoader 的 MODEL→KSampler、
CLIP→CLIPTextEncode×2，VAE 仍直接来自 CheckpointLoader。

## Pattern 演化

```text
Pattern Evolution

Basic:
    SD1.5 Text2Image (sd15-t2i-basic)

Extension:
    + LoRA (LoraLoader)

Result:
    New Pattern (sd15-t2i-lora)
```

## 与相邻模式的区分

| 模式 | 区别点 |
|---|---|
| sd15-t2i-basic | 无 LoraLoader，CLIP/MODEL 直连 CheckpointLoader |
| 多 LoRA 链式叠加 | 2 个以上 LoraLoader 首尾串联 |
| LoRA + ControlNet | 再增加 ControlNetLoader + ControlNetApply(Advanced) |
| 图生图 + LoRA | EmptyLatentImage → LoadImage + VAEEncode，denoise < 1.0 |

## 关键参数基准（本模式典型值）

- LoraLoader: strength_model 0.5~1.0（实测例 0.75）/ strength_clip 0.8~1.0（实测例 1.0）
- 采样（实测例）: dpmpp_2m + karras，30 步，cfg 7，denoise 1.0，768×768
- 负面词起步（实测例）: `(worst quality, low quality:1.4), (bad anatomy), text, watermark...`

## 来源实例

- comfyui_library/workflows/sd1.5/lora.png（2026-10-04 分析，8 节点，
  dreamshaper_8 + blindbox_V1Mix，ComfyUI 官方 LoRA 教程工作流）

## 学习价值

理解 LoRA 的注入点与作用面：它同时改写 MODEL 和 CLIP 两路、但不接管 VAE——
这解释了"为什么换 LoRA 不影响解码"。也是学习多 LoRA 串联、LoRA+ControlNet 等
复杂组合的基准形态。
