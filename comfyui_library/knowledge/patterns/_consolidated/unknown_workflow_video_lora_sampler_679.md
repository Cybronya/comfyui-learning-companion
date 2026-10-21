---
name: unknown_workflow_video_lora_sampler_679
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.823333
common_nodes: [BerniniStudio, CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SetNode, Text, TextConcatenate_UTK, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2074655037963460609.json, 视频生成/图生视频/2074532825533075457.json, 视频生成/图生视频/2074550169936420866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_679

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2074655037963460609.json、视频生成/图生视频/2074532825533075457.json、视频生成/图生视频/2074550169936420866.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SetNode`
- `Text`
- `TextConcatenate_UTK`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FlashVSR_SM_KSampler` —— 2/3 个有
- `FlashVSR_SM_Model` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `GoogleTranslator` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.05822e+09 | - | 2 | 92% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 67% |
| 采样算法 | 2 | 1 - 2 | 3 | 72% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.05822e+09，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 67%
- 采样算法 中位数 2，观测区间 1 - 2，3 个样本
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.14318e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
