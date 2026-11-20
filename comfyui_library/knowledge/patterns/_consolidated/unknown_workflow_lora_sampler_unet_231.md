---
name: unknown_workflow_lora_sampler_unet_231
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7275
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveInt, PrimitiveStringMultiline, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, ViggleRemakeConditioningByShenGun, ViggleRemakeLongVideoByShenGun, ViggleRemakeNoiseByShenGun]
problems: []
missing: []
members: [平台全量/H3-替换人物（长视频）_2119957792101584897.json, 平台全量/H3-替换人物（长视频）_2119999886761480193.json, 平台全量/H3-替换人物（长视频）_2120157977373143041.json, 视频生成/视频生视频/很好用的视频人物替换（长视频）Viggle-H3_2120172459239493633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_231

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/H3-替换人物（长视频）_2119957792101584897.json、平台全量/H3-替换人物（长视频）_2119999886761480193.json、平台全量/H3-替换人物（长视频）_2120157977373143041.json、视频生成/视频生视频/很好用的视频人物替换（长视频）Viggle-H3_2120172459239493633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `ViggleRemakeConditioningByShenGun`
- `ViggleRemakeLongVideoByShenGun`
- `ViggleRemakeNoiseByShenGun`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 3/4 个有
- `JDCN_VHSFileMover` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `Vignette` —— 1/4 个有
- `easy saveText` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
