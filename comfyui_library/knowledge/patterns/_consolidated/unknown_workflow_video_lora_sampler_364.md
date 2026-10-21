---
name: unknown_workflow_video_lora_sampler_364
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.513
common_nodes: [BasicScheduler, CLIPLoader, GetNode, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json, 视频生成/图生视频/poster animation_2094321304538279938.json, 视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json, 视频生成/文生视频/MiniMax+H3文生视频_2089205361046810625.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094359561212882945.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094381288823287810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_364

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json、视频生成/图生视频/poster animation_2094321304538279938.json、视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json、视频生成/文生视频/MiniMax+H3文生视频_2089205361046810625.json、视频生成/文生视频/MiniMax-H3开源 文生视频_2094359561212882945.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `BasicGuider` —— 5/6 个有
- `ComfyMathExpression` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `Text` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `VHS_LoadVideoFFmpeg` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `JjkText` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MiniMaxH3ReferenceToVideo` —— 2/6 个有
- `CFGGuider` —— 1/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `QwenH3PromptLocal` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
