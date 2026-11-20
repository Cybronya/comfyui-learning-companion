---
name: unknown_workflow_video_sampler_unet_43
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.803143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-视频模仿_2088128829062729729.json, 视频生成/图生视频/MiniMaxH3视频编辑 换装+动作迁移+全节点注释_2088511380671520770.json, 视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2114523574005493761.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json, 视频生成/图生视频/text（测试用）_2108791779993677825.json, 音频生成/音频生成/minimax_h3 参考图生视频+sage加速_2085965890079776770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-视频模仿_2088128829062729729.json、视频生成/图生视频/MiniMaxH3视频编辑 换装+动作迁移+全节点注释_2088511380671520770.json、视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2114523574005493761.json、视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json、视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `EasyCache` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `VRAM_Debug` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Text` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `ttN float` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
