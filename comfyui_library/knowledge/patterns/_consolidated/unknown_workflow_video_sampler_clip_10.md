---
name: unknown_workflow_video_sampler_clip_10
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.746652
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2016499156017221633.json, 视频生成/图生视频/2016457012112007170.json, 视频生成/图生视频/1991465239868817409.json, 视频生成/图生视频/2040996978963783681.json, 视频生成/图生视频/2013524441493413889.json, 视频生成/图生视频/2011778743831896065.json, 视频生成/图生视频/1991464228328521730.json, 视频生成/图生视频/1998932620186673154.json, 视频生成/图生视频/1990820621133225985.json, 视频生成/图生视频/1986358473883582465.json, 视频生成/图生视频/1998939454473691137.json, 视频生成/图生视频/1987947016699449345.json, 视频生成/图生视频/1991088759945146369.json, 视频生成/图生视频/2001883203667390466.json, 视频生成/图生视频/2028082455047053313.json, 视频生成/图生视频/2035642798367580161.json, 视频生成/图生视频/2040996941684805634.json, 视频生成/图生视频/2041144753068183554.json, 视频生成/图生视频/2041411103518887938.json, 视频生成/图生视频/2037879227361533953.json, 视频生成/图生视频/2035642836963565570.json, 视频生成/图生视频/1991074720969891842.json, 视频生成/图生视频/2042534334439100418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/2016499156017221633.json、视频生成/图生视频/2016457012112007170.json、视频生成/图生视频/1991465239868817409.json、视频生成/图生视频/2040996978963783681.json、视频生成/图生视频/2013524441493413889.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 21/23 个有
- `PathchSageAttentionKJ` —— 21/23 个有
- `Seed (rgthree)` —— 21/23 个有
- `easy cleanGpuUsed` —— 21/23 个有
- `PainterI2V` —— 19/23 个有
- `RunningHub Deepcleaner` —— 19/23 个有
- `easy showAnything` —— 19/23 个有
- `CR Prompt Text` —— 18/23 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 15/23 个有
- `Float` —— 14/23 个有
- `ImageFromBatch+` —— 13/23 个有
- `MathExpression|pysssss` —— 12/23 个有
- `easy anythingIndexSwitch` —— 12/23 个有
- `AILab_QwenVL` —— 11/23 个有
- `RH_LLMAPI_NODE` —— 11/23 个有
- `WanImageToVideo` —— 9/23 个有
- `CR Text` —— 8/23 个有
- `LoraLoaderModelOnly` —— 8/23 个有
- `ShellAgentPluginOutputText` —— 8/23 个有
- `llama_cpp_instruct_adv` —— 8/23 个有
- `llama_cpp_model_loader` —— 8/23 个有
- `llama_cpp_parameters` —— 8/23 个有
- `AddLabel` —— 7/23 个有
- `ImageConcanate` —— 7/23 个有
- `PDIMAGE_LongerSize` —— 5/23 个有
- `ProcessString` —— 2/23 个有
- `ImageConcatMulti` —— 1/23 个有
- `MemoryCleaner` —— 1/23 个有
- `Text Concatenate` —— 1/23 个有
- `wanBlockSwap` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 23 | 91% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 23 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 23 | 86% |
| 调度器 | euler_ancestral | - | 23 | 87% |
| 重绘幅度 | simple | - | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，23 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，23 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，23 个样本，取值集中（一致性 86%）
- 调度器 最常用 euler_ancestral，23 个样本，一致性 87%
- 重绘幅度 最常用 simple，23 个样本，一致性 100%
