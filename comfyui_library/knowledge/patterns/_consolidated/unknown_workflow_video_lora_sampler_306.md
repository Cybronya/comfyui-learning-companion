---
name: unknown_workflow_video_lora_sampler_306
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.580444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelPatchTorchSettings, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json, 平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json, 平台全量/MinimaxH3_Pika_H3Flex-参考生视频（基础对比）工作流_2117643617908121601.json, 平台全量/MinimaxH3_人物替换lora 版_2111131374135635970.json, 平台全量/MinimaxH3_人物替换lora 版_2112906331517710337.json, 视频生成/图生视频/MinimaxH3_2Stage-NVRegen2k-新二采工作流_2116016996398751745.json, 视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json, 视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json, 视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_306

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json、平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json、平台全量/MinimaxH3_Pika_H3Flex-参考生视频（基础对比）工作流_2117643617908121601.json、平台全量/MinimaxH3_人物替换lora 版_2111131374135635970.json、平台全量/MinimaxH3_人物替换lora 版_2112906331517710337.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelPatchTorchSettings`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 8/9 个有
- `MiniMaxH3SigmaShift` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `SeedNode` —— 8/9 个有
- `StringConcatenate` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/9 个有
- `Label (rgthree)` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `VedaSparseAttention` —— 5/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `MMH3LatentUpscaleWithModelParams` —— 3/9 个有
- `MMH3SpatialSplitParams` —— 3/9 个有
- `MMH3TemporalSplitParams` —— 3/9 个有
- `MMH3UltimateUpscale` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `easy clearCacheAll` —— 3/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `RMBG` —— 2/9 个有
- `VAEDecodeTiled` —— 2/9 个有
- `XB_CanvasLabel` —— 2/9 个有
- `floatToInt _O` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `MiniMaxH3VAEDecodeFast` —— 1/9 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SolAttnPatch` —— 1/9 个有
- `Textbox` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
