---
name: image_to_image_controlnet_upscale_lora_5
type: Image To Image
frequency: 8
level: strong
coverage: 0.615875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ConstrainImage|pysssss, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, FluxUnionControlNetApply, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TextBox, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Alan测-图片8K放大_1980195629232197633.json, 图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json, 图片生成/图生图/图片8K高清放大_2018489327587692546.json, 图片生成/图生图/最新4k高清放大  超清晰 解决kontext模糊问题_1934512708182036482.json, 图片生成/图生图/终极高端 4K放大工作流_1943306656119726082.json, 平台全量/图片8K放大_1942777181443698690.json, 平台全量/图片8K放大_1942784112794996738.json, 平台全量/图片8K放大_1983733255176429569.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Alan测-图片8K放大_1980195629232197633.json、图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json、图片生成/图生图/图片8K高清放大_2018489327587692546.json、图片生成/图生图/最新4k高清放大  超清晰 解决kontext模糊问题_1934512708182036482.json、图片生成/图生图/终极高端 4K放大工作流_1943306656119726082.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `FluxUnionControlNetApply`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextBox`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 7/8 个有
- `Float` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `MathExpression|pysssss` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `StringFunction|pysssss` —— 7/8 个有
- `TTPlanet_Tile_Preprocessor_Simple` —— 7/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `ColorMatch` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy imageSize` —— 1/8 个有
- `easy imageSizeBySide` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.6 - 0.8 | 7 | 91% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.6 - 0.8，7 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
