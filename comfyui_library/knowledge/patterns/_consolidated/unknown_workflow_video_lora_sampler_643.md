---
name: unknown_workflow_video_lora_sampler_643
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.576333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, RH_LLMAPI_Pro_Node, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2034288165581758466.json, 视频生成/图生视频/2045775730209984513.json, 视频生成/图生视频/2025905016736845825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_643

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2034288165581758466.json、视频生成/图生视频/2045775730209984513.json、视频生成/图生视频/2025905016736845825.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `ShellAgentPluginOutputText` —— 1/3 个有
- `TT_img_enc_v2` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 4 - 8 | 3 | 72% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 8，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
