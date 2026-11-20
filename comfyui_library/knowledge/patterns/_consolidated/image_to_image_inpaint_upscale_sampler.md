---
name: image_to_image_inpaint_upscale_sampler
type: Image To Image
frequency: 18
level: strong
coverage: 0.917056
common_nodes: [BasicScheduler, CFGNorm, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, DetailDaemonSamplerNode, Florence2ModelLoader, Florence2Run, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, ImpactMakeAnyList, InpaintModelConditioning, KSampler, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, PreviewBridge, QwenMultiangleCameraNode, SamplerCustom, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy promptConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2013834742021492738.json, 图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2017084440501030913.json, 图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2020717254878437377.json, 图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2021398281284231170.json, 图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2048664696554786818.json, 图片生成/图生图/qwen-edit-2511-多视角生成人物角色_2019578379158167554.json, 图片生成/图生图/qwen-edit-2511模型应用：多视角控制生成技术实现高效人物角色设计与创作_2057375800537731074.json, 图片生成/图生图/万能相机视角 人物角色设计 镜头自由调节 qwen-edit-2511 多视角控制生成  提升角色一_2046107252137922562.json, 图片生成/图生图/摄影机角度 万能相机视角 qwen-edit-2511 人物角色一致+镜头自由调节 +多视角控制生成_2019573056892571649.json, 平台全量/qwen-edit-2511-多视角控制生成-人物角色设计_2009940290831917057.json, 平台全量/qwen-edit-2511-自定义人物角度姿势_2026504794789122049.json, 平台全量/qwen-edit-2511模型应用：多视角控制生成技术实现高效人物角色设计与创作_2015284735433515009.json, 平台全量/qwen-edit：多视角控制，精准控制视角，保持人物一致性，AI漫剧角色控制，AI短剧角色控制_2019380456378081281.json, 平台全量/万能相机视角 人物角色设计 镜头自由调节 qwen-edit-2511 多视角控制生成  提升角色一_2013844908259418114.json, 平台全量/多视角控制生成 人物角色设计 高度一致性qwen-edit 人物全方位视角转换_2019673364209606657.json, 平台全量/多视角控制，保持人物一致性_2021101847334887425.json, 平台全量/摄影机角度 万能相机视角 qwen-edit-2511 人物角色一致+镜头自由调节 +多视角控制生成_2015997984399433729.json, 平台全量/🤹‍♂️老许Gary：Qwen-edit-2511-多视角控制生成-人物角色设计_2025099856708116482.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2013834742021492738.json、图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2017084440501030913.json、图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2020717254878437377.json、图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2021398281284231170.json、图片生成/图生图/qwen-edit-2511-多视角控制生成-人物角色设计_2048664696554786818.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `ImpactMakeAnyList`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
- `QwenMultiangleCameraNode`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 17/18 个有
- `LoraLoaderModelOnly` —— 15/18 个有
- `Any Switch (rgthree)` —— 14/18 个有
- `Fast Groups Bypasser (rgthree)` —— 11/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/18 个有
- `PreviewImage` —— 2/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler_ancestral | - | 18 | 100% |
| 调度器 | sgm_uniform | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
