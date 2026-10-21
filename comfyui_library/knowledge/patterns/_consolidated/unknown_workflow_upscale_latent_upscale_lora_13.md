---
name: unknown_workflow_upscale_latent_upscale_lora_13
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.840067
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json, 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json, 视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json, 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json, 视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json, 视频生成/文生视频/LTX-2.3-文生视频_2031191268642004993.json, 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json, 视频生成/文生视频/LTX-2文生视频ComfyUI官方流快速ltx2模型fp8加速模型带音效_2012003240623218689.json, 视频生成/文生视频/LTX-2文生视频Plus运行模式专用_2008537121744752642.json, 视频生成/文生视频/LTX-2文生视频工作流_2008796662071824386.json, 视频生成/文生视频/LTX-2文生视频工作流_2009245499412455426.json, 视频生成/文生视频/LTX-2文生视频提示词优化版_2009586018684510210.json, 视频生成/文生视频/LTX2.0-低显存版-自动提示词-动态强化-运镜加速-文生视频V1_2011665816391000065.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频_2029767452879491074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json、视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json、视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json、视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json、视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `PrimitiveInt` —— 14/15 个有
- `SaveVideo` —— 14/15 个有
- `VAEDecode` —— 9/15 个有
- `ManualSigmas` —— 8/15 个有
- `PreviewAny` —— 8/15 个有
- `DualCLIPLoader` —— 7/15 个有
- `KSampler` —— 7/15 个有
- `TextGenerateLTX2Prompt` —— 7/15 个有
- `Int` —— 4/15 个有
- `CR Prompt Text` —— 3/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `VHS_VideoCombine` —— 3/15 个有
- `CustomAddLabel` —— 2/15 个有
- `Label (rgthree)` —— 2/15 个有
- `LayerUtility: PurgeVRAM V2` —— 2/15 个有
- `SimpleMath+` —— 2/15 个有
- `Text` —— 2/15 个有
- `easy anythingIndexSwitch` —— 2/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `数学运算_孤海` —— 2/15 个有
- `AddLabel` —— 1/15 个有
- `Any To Any` —— 1/15 个有
- `CM_IntToFloat` —— 1/15 个有
- `ImpactExecutionOrderController` —— 1/15 个有
- `JWInteger` —— 1/15 个有
- `JoinStrings` —— 1/15 个有
- `MultiTextConcatenate` —— 1/15 个有
- `Qwen3_VQA` —— 1/15 个有
- `ShowText` —— 1/15 个有
- `TextInput_` —— 1/15 个有
- `Textbox` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `VAELoader` —— 1/15 个有
- `VAELoaderKJ` —— 1/15 个有
- `VRAMReserver` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 7 | 100% |
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/15 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
