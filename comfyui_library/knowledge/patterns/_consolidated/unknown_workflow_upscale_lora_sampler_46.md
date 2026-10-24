---
name: unknown_workflow_upscale_lora_sampler_46
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CheckpointLoaderSimple, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, LoraLoaderModelOnly, RandomNoise, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/seedvr2图片去ai感_1986382767250407425.json, 图片生成/图生图/去AI化人物皮肤质感工作流_1971855002417426434.json, 图片生成/图生图/去AI化工作流-一键去除AI感-更多纹理v1_1971757026890149890.json, 图片生成/图生图/去AI感-增加皮肤质感_1956564091567525890.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/seedvr2图片去ai感_1986382767250407425.json、图片生成/图生图/去AI化人物皮肤质感工作流_1971855002417426434.json、图片生成/图生图/去AI化工作流-一键去除AI感-更多纹理v1_1971757026890149890.json、图片生成/图生图/去AI感-增加皮肤质感_1956564091567525890.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ColorMatch` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `CR Upscale Image` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `ImpactImageBatchToImageList` —— 1/4 个有
- `Joy_caption_two` —— 1/4 个有
- `Joy_caption_two_load` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TTP_Image_Assy` —— 1/4 个有
- `TTP_Image_Tile_Batch` —— 1/4 个有
- `TTP_Tile_image_size` —— 1/4 个有
- `UltimateSDUpscaleNoUpscale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.7 - 0.8 | 4 | 94% |
| LoRA 文本强度 | 0.8 | 0.7 - 0.8 | 4 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.7 - 0.8，4 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 0.8，观测区间 0.7 - 0.8，4 个样本，取值集中（一致性 94%）
