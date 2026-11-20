---
name: image_to_image_controlnet_inpaint_sampler_3
type: Image To Image
frequency: 11
level: strong
coverage: 0.877545
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json, 图片生成/图生图/千问扩图工作流 (1)_2009525416305893378.json, 图片生成/图生图/千问扩图工作流_2005599741033541633.json, 图片生成/图生图/千问扩图工作流_2010274187272785921.json, 图片生成/图生图/啊癫 千问【最新】扩图工作流_2026689029210644481.json, 图片生成/文生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_1966334484977233922.json, 图片生成/文生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2004037122640257026.json, 图片生成/文生图/千问局部重绘工作流_1989153552679448577.json, 图片生成/文生图/千问扩图工作流_1989155186948059137.json, 平台全量/千问局部重绘（4步加速）_1980916528013070337.json, 平台全量/工作流千问篇3-Qwen千问局部重绘-给我改图_2022220738404552706.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json、图片生成/图生图/千问扩图工作流 (1)_2009525416305893378.json、图片生成/图生图/千问扩图工作流_2005599741033541633.json、图片生成/图生图/千问扩图工作流_2010274187272785921.json、图片生成/图生图/啊癫 千问【最新】扩图工作流_2026689029210644481.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `ImagePadForOutpaint` —— 8/11 个有
- `ModelSamplingAuraFlow` —— 8/11 个有
- `PDImageResizeV2` —— 6/11 个有
- `UnetLoaderGGUF` —— 5/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `CLIPLoaderGGUF` —— 3/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `ImageAndMaskPreview` —— 3/11 个有
- `ImageUpscaleWithModel` —— 2/11 个有
- `UpscaleModelLoader` —— 2/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 11 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，11 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
