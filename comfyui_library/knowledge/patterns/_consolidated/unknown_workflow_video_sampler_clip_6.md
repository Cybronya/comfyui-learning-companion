---
name: unknown_workflow_video_sampler_clip_6
type: Unknown Workflow
frequency: 34
level: strong
coverage: 0.550529
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, Qwen3_VQA, RIFE VFI, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMultiFrameRefToVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2014265422324961282.json, 视频生成/图生视频/2018698814936322049.json, 视频生成/图生视频/2008822660024766465.json, 视频生成/图生视频/2013245463608168449.json, 视频生成/图生视频/2018147957211664386.json, 视频生成/图生视频/单图+双图+三图版+最强动漫模型DaSiWa8.1视频流_2084164733128761346.json, 视频生成/图生视频/2058921608584192002.json, 视频生成/图生视频/2058925648005128194.json, 视频生成/图生视频/2058926947182403586.json, 视频生成/图生视频/2058930825034559489.json, 视频生成/图生视频/2071783993749626881.json, 视频生成/图生视频/2057702930412822529.json, 视频生成/图生视频/2008533266399240194.json, 视频生成/图生视频/2058913924552159233.json, 视频生成/图生视频/2058930743153352705.json, 视频生成/图生视频/2058931179931389953.json, 视频生成/图生视频/2069752300628959233.json, 视频生成/图生视频/2069752441821814785.json, 视频生成/图生视频/2071417391518670850.json, 视频生成/图生视频/2071775950022467586.json, 视频生成/图生视频/2071849511944806402.json, 视频生成/图生视频/2071849751959662594.json, 视频生成/图生视频/2071857804616495105.json, 视频生成/图生视频/2079761122793709569.json, 视频生成/图生视频/2079851983518920705.json, 视频生成/图生视频/2071399792839843842.json, 视频生成/图生视频/2070316679850188801.json, 视频生成/图生视频/图生视频-老照片动起来_2085169884861919234.json, 视频生成/图生视频/1993305632644284418.json, 视频生成/图生视频/2026126514126852097.json, 视频生成/图生视频/2057352662831685634.json, 视频生成/图生视频/2013098243374190593.json, 视频生成/图生视频/2082301874304274433.json, 视频生成/图生视频/2071793684768714753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（视频生成/图生视频/2014265422324961282.json、视频生成/图生视频/2018698814936322049.json、视频生成/图生视频/2008822660024766465.json、视频生成/图生视频/2013245463608168449.json、视频生成/图生视频/2018147957211664386.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 34 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `Qwen3_VQA`
- `RIFE VFI`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMultiFrameRefToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 33/34 个有
- `PainterI2V` —— 33/34 个有
- `WanFirstLastFrameToVideo` —— 33/34 个有
- `easy cleanGpuUsed` —— 32/34 个有
- `Fast Groups Bypasser (rgthree)` —— 26/34 个有
- `DuckHideNode` —— 23/34 个有
- `SaveImage` —— 23/34 个有
- `TT_img_enc` —— 23/34 个有
- `TT_img_enc_v2` —— 23/34 个有
- `PreviewImage` —— 10/34 个有
- `SimpleMath+` —— 8/34 个有
- `Fast Groups Muter (rgthree)` —— 7/34 个有
- `GetImagesFromBatchIndexed` —— 3/34 个有
- `LoraLoaderModelOnly` —— 2/34 个有
- `JjkText` —— 1/34 个有
- `RH_LLMAPI_NODE` —— 1/34 个有
- `wanBlockSwap` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 34 | 76% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 34 | 85% |
| 采样算法 | 1 | 1 - 1 | 34 | 100% |
| 调度器 | euler | - | 34 | 100% |
| 重绘幅度 | simple | - | 34 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，34 个样本，一致性 76%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，34 个样本，取值集中（一致性 85%）
- 采样算法 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，34 个样本，一致性 100%
- 重绘幅度 最常用 simple，34 个样本，一致性 97%
