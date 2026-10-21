---
name: unknown_workflow_video_sampler_clip_17
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.767778
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, Float, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1993272567492444161.json, 视频生成/图生视频/2010957966706479106.json, 视频生成/图生视频/2020428290829328386.json, 视频生成/图生视频/2028397486544527362.json, 视频生成/图生视频/2028678704204881921.json, 视频生成/图生视频/2028683653529735169.json, 视频生成/图生视频/2028399847149146114.json, 视频生成/图生视频/1991085974646272001.json, 视频生成/图生视频/1987947024861564930.json, 视频生成/图生视频/2036976880821215234.json, 视频生成/图生视频/2062141489110667266.json, 视频生成/图生视频/2025914003163189250.json, 视频生成/图生视频/2041400574976991233.json, 视频生成/图生视频/2041128581908140034.json, 视频生成/图生视频/2041143697240231938.json, 视频生成/图生视频/2037015059473371137.json, 视频生成/图生视频/2040996963277082626.json, 视频生成/图生视频/2035642903317454849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1993272567492444161.json、视频生成/图生视频/2010957966706479106.json、视频生成/图生视频/2020428290829328386.json、视频生成/图生视频/2028397486544527362.json、视频生成/图生视频/2028678704204881921.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Float`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 17/18 个有
- `easy anythingIndexSwitch` —— 17/18 个有
- `easy showAnything` —— 17/18 个有
- `ColorMatch` —— 16/18 个有
- `ImageFromBatch+` —— 16/18 个有
- `ImageScaleBy` —— 16/18 个有
- `MathExpression|pysssss` —— 16/18 个有
- `RunningHub Deepcleaner` —— 16/18 个有
- `SaveImage` —— 16/18 个有
- `Pick From Batch (mtb)` —— 15/18 个有
- `PreviewImage` —— 15/18 个有
- `PainterI2V` —— 11/18 个有
- `AILab_QwenVL` —— 9/18 个有
- `RH_LLMAPI_NODE` —— 9/18 个有
- `CR Text` —— 8/18 个有
- `ShellAgentPluginOutputText` —— 8/18 个有
- `llama_cpp_instruct_adv` —— 8/18 个有
- `llama_cpp_model_loader` —— 8/18 个有
- `llama_cpp_parameters` —— 8/18 个有
- `LoraLoaderModelOnly` —— 7/18 个有
- `DuckHideNode` —— 5/18 个有
- `TT_img_enc` —— 5/18 个有
- `TT_img_enc_v2` —— 5/18 个有
- `Int` —— 3/18 个有
- `Anything Everywhere` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 18 | 100% |
| 采样算法 | 1 | 1 - 1 | 18 | 100% |
| 调度器 | euler_ancestral | - | 18 | 100% |
| 重绘幅度 | simple | - | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，18 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，18 个样本，一致性 100%
- 重绘幅度 最常用 simple，18 个样本，一致性 100%
