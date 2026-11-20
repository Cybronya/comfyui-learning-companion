---
name: text_to_image_upscale_lora_sampler_35
type: Text To Image
frequency: 7
level: weak
coverage: 0.942571
common_nodes: [AIO_Preprocessor, BodyRatioMapperSDPoseRender, CLIPLoader, CLIPTextEncode, CR Image Input Switch, CR Model Input Switch, CR Text, CR Text Concatenate, CheckpointLoaderSimple, ConditioningZeroOut, DisTorchPurgeVRAMV2, EmptyLatentImage, Float, FluxKontextMultiReferenceLatentMethod, GetImageSize, INTConstant, ImageUpscaleWithModel, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, Krea2OstrisEditModelPatch, Krea2T-Enhancer-Advanced, LoadImage, LoraLoaderModelOnly, RHHiddenNodes, SDPoseKeypointExtractor, SaveImage, ShowText|pysssss, TextEncodeKrea2OstrisEdit, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2反推控制洗图流 ControlNet深度姿态可选高清放大_2099180072275111938.json, 图片生成/图生图/Krea2反推控制洗图流 ControlNet深度姿态可选高清放大_2099559000349171713.json, 图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json, 图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2096775581680619522.json, 图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2096881746125090818.json, 图片生成/图生图/Krea2反推控制洗图流｜ControlNet深度姿态高清放大_2097089917624082433.json, 图片生成/图生图/Krea2反推洗图高清流｜ControlNet深度姿态随心选，洗图不糊细节_2099522893767073794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2反推控制洗图流 ControlNet深度姿态可选高清放大_2099180072275111938.json、图片生成/图生图/Krea2反推控制洗图流 ControlNet深度姿态可选高清放大_2099559000349171713.json、图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json、图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2096775581680619522.json、图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2096881746125090818.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `BodyRatioMapperSDPoseRender`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Image Input Switch`
- `CR Model Input Switch`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DisTorchPurgeVRAMV2`
- `EmptyLatentImage`
- `Float`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `INTConstant`
- `ImageUpscaleWithModel`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `Krea2OstrisEditModelPatch`
- `Krea2T-Enhancer-Advanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `SDPoseKeypointExtractor`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `孤海注释` —— 4/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 7 | 4% |
| 高度 | 80 | 80 - 1024 | 7 | 4% |
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 0.6 - 1 | 7 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，7 个样本
- 高发问题（18/7 个样本）：Steps较低可能导致细节不足
