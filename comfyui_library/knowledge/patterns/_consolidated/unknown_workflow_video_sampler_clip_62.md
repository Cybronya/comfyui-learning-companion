---
name: unknown_workflow_video_sampler_clip_62
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8378
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/Remix_V3+Qwen3.5提示词反推_I2V_2039893692558876673.json, 视频生成/图生视频/Wan2.2 Remix V3-效果好_2036675075717472258.json, 视频生成/图生视频/Wan2.2 Remix V3.0--Qwen3.5自动化图生视频_2035931554823806977.json, 视频生成/图生视频/Wan2.2 Remix V3_2036102577590374402.json, 视频生成/图生视频/Wan2.2 Remix V3_2036614477726097410.json, 视频生成/图生视频/【阿良绘】Dasiwa V10+Qwen3.5图生视频自动提示词 （N版）_2041128581908140034.json, 视频生成/图生视频/（N SFW）Dasiwa V10+Qwen3.5图生视频自动提示词工作流V1_2041143697240231938.json, 视频生成/图生视频/（N SFW）Remix V3+Qwen3.5图生视频自动提示词工作流V1_2037015059473371137.json, 视频生成/图生视频/（自用）Dasiwa V10+Qwen3.5图生视频自动提示词工作流V1（N版）_2040996963277082626.json, 视频生成/图生视频/（自用）Remix V3+Qwen3.5图生视频自动提示词工作流V1（N版）_2035642903317454849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Remix_V3+Qwen3.5提示词反推_I2V_2039893692558876673.json、视频生成/图生视频/Wan2.2 Remix V3-效果好_2036675075717472258.json、视频生成/图生视频/Wan2.2 Remix V3.0--Qwen3.5自动化图生视频_2035931554823806977.json、视频生成/图生视频/Wan2.2 Remix V3_2036102577590374402.json、视频生成/图生视频/Wan2.2 Remix V3_2036614477726097410.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `Float` —— 9/10 个有
- `LayerUtility: PurgeVRAM` —— 9/10 个有
- `ImageFromBatch+` —— 7/10 个有
- `RunningHub Deepcleaner` —— 6/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `ShellAgentPluginOutputText` —— 6/10 个有
- `easy anythingIndexSwitch` —— 6/10 个有
- `DuckHideNode` —— 5/10 个有
- `ImageScaleBy` —— 5/10 个有
- `SaveImage` —— 5/10 个有
- `TT_img_enc` —— 5/10 个有
- `TT_img_enc_v2` —— 5/10 个有
- `ColorMatch` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `Pick From Batch (mtb)` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `FL_RIFE` —— 3/10 个有
- `RTXVideoSuperResolution` —— 3/10 个有
- `Anything Everywhere` —— 1/10 个有
- `Load Image From Url (mtb)` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `String` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler_ancestral | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
