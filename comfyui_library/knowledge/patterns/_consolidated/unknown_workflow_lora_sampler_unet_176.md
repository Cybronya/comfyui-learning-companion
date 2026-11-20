---
name: unknown_workflow_lora_sampler_unet_176
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86325
common_nodes: [CLIPLoader, CR Text, ComfySwitchNode, DF_Integer, ImageScaleToTotalPixels, JWImageResizeByLongerSide, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, QwenImage21Cache, RegexMatch, RegexReplace, SaveImage, SeedNode, SplitImageWithAlpha, StringFormat, Text, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json, 图片生成/图生图/Qwen-Image-2.1 换装V2（高一致性_无偏移）_2107069164946026498.json, 图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json, 图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_176

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json、图片生成/图生图/Qwen-Image-2.1 换装V2（高一致性_无偏移）_2107069164946026498.json、图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json、图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ComfySwitchNode`
- `DF_Integer`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `QwenImage21Cache`
- `RegexMatch`
- `RegexReplace`
- `SaveImage`
- `SeedNode`
- `SplitImageWithAlpha`
- `StringFormat`
- `Text`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Compare (mtb)` —— 3/4 个有
- `孤海注释` —— 2/4 个有
- `GoohaiDisplayAny` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `SDPoseOODLoader` —— 1/4 个有
- `SDPoseOODProcessor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
