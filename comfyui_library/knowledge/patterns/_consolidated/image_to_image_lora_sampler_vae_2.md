---
name: image_to_image_lora_sampler_vae_2
type: Image To Image
frequency: 18
level: strong
coverage: 0.862
common_nodes: [CFGNorm, DepthAnythingPreprocessor, ImagePadForOutpaint, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, OpenposePreprocessor, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2Klein9b产品自动加背景_2054142521697161218.json, 图片生成/图生图/KIKI-QW改图流-溶图_1987362101750640641.json, 图片生成/图生图/Qwen-Edit-2509 多功能 合集 Qwen Edit 2509_1996398880864485378.json, 图片生成/图生图/Qwen-Edit-2509 测试_2002977592728797186.json, 图片生成/图生图/Qwen-Edit-2509-光影消除_1993375065609879554.json, 图片生成/图生图/Qwen-Edit-2509-加强溶图_1991770944909963265.json, 图片生成/图生图/Qwen-Edit-2509-去除光斑_过曝_欠曝修复_1986847676127973378.json, 图片生成/图生图/Qwen-Edit-2509-多人物生成_1985510042604609538.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换Rh在线流程-官方多角度测试流程_1987741808379760641.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_1992134691987804162.json, 图片生成/图生图/Qwen-Edit-2509-多角度灯光_1990093672173719553.json, 图片生成/图生图/Qwen-Edit-2509-多角度灯光_2001200568754466817.json, 图片生成/图生图/Qwen-Edit-2509-溶图_1992867249648365570.json, 图片生成/图生图/Qwen-Edit-2509-白底图转场景-cr大熊_1998600515145621506.json, 图片生成/图生图/Qwen-Edit-2509-白底图转场景_1985635336372068353.json, 图片生成/图生图/Qwen-Edit-2509-白膜转材质_1988543268420018177.json, 图片生成/图生图/Qwen-Edit-2509人物打光_1993482633977987073.json, 图片生成/图生图/Qwen-Edit-2509人物打光_2039282780902789122.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Flux2Klein9b产品自动加背景_2054142521697161218.json、图片生成/图生图/KIKI-QW改图流-溶图_1987362101750640641.json、图片生成/图生图/Qwen-Edit-2509 多功能 合集 Qwen Edit 2509_1996398880864485378.json、图片生成/图生图/Qwen-Edit-2509 测试_2002977592728797186.json、图片生成/图生图/Qwen-Edit-2509-光影消除_1993375065609879554.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `DepthAnythingPreprocessor`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 17/18 个有
- `Image Comparer (rgthree)` —— 17/18 个有
- `Mask Fill Holes` —— 17/18 个有
- `ModelPatchLoader` —— 17/18 个有
- `QwenImageDiffsynthControlnet` —— 17/18 个有
- `TextEncodeQwenImageEditPlus` —— 17/18 个有
- `CLIPLoader` —— 14/18 个有
- `UNETLoader` —— 14/18 个有
- `LoadDiffusionModelShared //Inspire` —— 4/18 个有
- `LoadTextEncoderShared //Inspire` —— 4/18 个有
- `ConditioningZeroOut` —— 2/18 个有
- `CFGGuider` —— 1/18 个有
- `CLIPTextEncode` —— 1/18 个有
- `Canny` —— 1/18 个有
- `EmptyFlux2LatentImage` —— 1/18 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/18 个有
- `Flux2Scheduler` —— 1/18 个有
- `GetImageSize` —— 1/18 个有
- `Int` —— 1/18 个有
- `KSamplerSelect` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `RandomNoise` —— 1/18 个有
- `ReferenceLatent` —— 1/18 个有
- `SamplerCustomAdvanced` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 18 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，18 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
