---
name: unknown_workflow_lora_sampler_unet_60
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.946636
common_nodes: [BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, LTXVSeparateAVLatent, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, TaoMateHDProgressiveSampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/TaomateHD_文生视频（极速版）_2119698490740789249.json, 平台全量/h3文生视频-taomateHD_t2va_2117920372988407810.json, 平台全量/taomate minimax h3加速工作流_2118896021295161345.json, 平台全量/taomateHD-全能参考_2117917103587155970.json, 平台全量/taomateHD_ 文生视频_2117937084781649921.json, 平台全量/taomateHD_t2va 文生视频_2117921003539091458.json, 平台全量/taomateHD_t2va_2117848995157602305.json, 平台全量/taomateHD卷视频速度一流-支持图生视频_2117890348621066242.json, 平台全量/taomateHD参考图生视频-快速1080p_2117939962338439170.json, 平台全量/taomateHD参考生视频（快速1080p）_2117848980364292097.json, 平台全量/taomateHD参考生视频（快速1080p）_2117918320610603009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/TaomateHD_文生视频（极速版）_2119698490740789249.json、平台全量/h3文生视频-taomateHD_t2va_2117920372988407810.json、平台全量/taomate minimax h3加速工作流_2118896021295161345.json、平台全量/taomateHD-全能参考_2117917103587155970.json、平台全量/taomateHD_ 文生视频_2117937084781649921.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `TaoMateHDProgressiveSampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `ModelPreviewOverrideKJ` —— 9/11 个有
- `MiniMaxH3ImageToVideo` —— 6/11 个有
- `MiniMaxH3ReferenceToVideo` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `LoadAudio` —— 2/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `StringTrim` —— 1/11 个有
- `TextEncodeFibo2` —— 1/11 个有
- `TrimAudio` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
