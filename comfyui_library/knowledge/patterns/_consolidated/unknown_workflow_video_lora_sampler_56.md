---
name: unknown_workflow_video_lora_sampler_56
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.44735
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, FL_RIFE, Fast Groups Bypasser (rgthree), INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2034182397939421186.json, 视频生成/图生视频/2028858830699892737.json, 视频生成/图生视频/Wan2.2优化版全自动视频生成器：万能视频制作图生视频工作流_2037840738377015297.json, 视频生成/图生视频/2038834532652163073.json, 视频生成/图生视频/2038927668770512898.json, 视频生成/图生视频/2033802610926428162.json, 视频生成/图生视频/Wan2.2优化版全自动视频生成器：万能视频制作工作流_2033833847380516865.json, 视频生成/图生视频/2057106642839359489.json, 视频生成/图生视频/2032814460473188353.json, 视频生成/图生视频/2029755512052523009.json, 视频生成/图生视频/2031051792376668162.json, 视频生成/图生视频/2046398368800317441.json, 视频生成/图生视频/2030287506285010945.json, 视频生成/图生视频/2037447795740774401.json, 视频生成/图生视频/2043261466400268290.json, 视频生成/图生视频/2028729107403513858.json, 视频生成/图生视频/2031903395463827458.json, 视频生成/图生视频/2037037456683442177.json, 视频生成/文生视频/WAN2.2全自动-万能视频生成器_2038992828327530498.json, 视频生成/文生视频/WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2034182397939421186.json、视频生成/图生视频/2028858830699892737.json、视频生成/图生视频/Wan2.2优化版全自动视频生成器：万能视频制作图生视频工作流_2037840738377015297.json、视频生成/图生视频/2038834532652163073.json、视频生成/图生视频/2038927668770512898.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/20 个有
- `RH_LLMAPI_Pro_Node` —— 17/20 个有
- `Int` —— 16/20 个有
- `PreviewAny` —— 16/20 个有
- `GetImageSizeRatio` —— 3/20 个有
- `Resize` —— 3/20 个有
- `DWPreprocessor` —— 1/20 个有
- `GetImageRangeFromBatch` —— 1/20 个有
- `MathExpression|pysssss` —— 1/20 个有
- `SaveImage` —— 1/20 个有
- `ShowText|pysssss` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 20 | 100% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler | - | 20 | 100% |
| 重绘幅度 | normal | - | 20 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，20 个样本，一致性 100%
- 重绘幅度 最常用 normal，20 个样本，一致性 95%
