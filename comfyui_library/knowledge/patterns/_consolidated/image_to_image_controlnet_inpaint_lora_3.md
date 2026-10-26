---
name: image_to_image_controlnet_inpaint_lora_3
type: Image To Image
frequency: 8
level: strong
coverage: 0.914375
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json, 图片生成/图生图/千问局部重绘工作流_2005603751757053954.json, 图片生成/图生图/千问局部重绘工作流_2010317606443552769.json, 图片生成/图生图/千问扩图工作流_2005599741033541633.json, 图片生成/图生图/千问扩图工作流_2010274187272785921.json, 图片生成/图生图/啊癫 千问【最新】扩图工作流_2026689029210644481.json, 图片生成/图生图/局部重绘王者对局（qwen与fill）_1967206477310070785.json, 图片生成/图生图/👾怪獸-局部重绘 Fill or 千问inpaintX双版本👾_1979927726142427137.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json、图片生成/图生图/千问局部重绘工作流_2005603751757053954.json、图片生成/图生图/千问局部重绘工作流_2010317606443552769.json、图片生成/图生图/千问扩图工作流_2005599741033541633.json、图片生成/图生图/千问扩图工作流_2010274187272785921.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/8 个有
- `ImageAndMaskPreview` —— 4/8 个有
- `ImagePadForOutpaint` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `PDImageResizeV2` —— 3/8 个有
- `DifferentialDiffusion` —— 2/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `FluxGuidance` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `InpaintModelConditioning` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 8 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，8 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
