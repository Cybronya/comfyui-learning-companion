---
name: unknown_workflow_sampler_unet_vae_23
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.817733
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax-H3 文生图片+全节点注释_2085181492325601281.json, 图片生成/文生图/MiniMaxH3 文生图文生图文生图文生图不是视频！2K加速版_2088278482991280130.json, 图片生成/文生图/MiniMaxH3 文生图！2K加速版！_2085238969377316866.json, 图片生成/文生图/MiniMaxH3开源 文生图文生图文生图 2K加速版_2088565003669557250.json, 图片生成/文生图/MiniMaxH3开源 文生图文生图文生图 2K加速版_2090436462390108161.json, 图片生成/文生图/MiniMaxH3开源版 文生图 2K加速版_2085323844386123777.json, 图片生成/文生图/MiniMaxH3开源版 文生图 2K加速版_2085326821125615617.json, 图片生成/文生图/MiniMax_H3 文生图-2K_2085311261709000706.json, 视频生成/图生视频/MinimaxI2V_2084500141607841794.json, 视频生成/图生视频/Minimax_h3_r2v图生视频_2084277716307767297.json, 视频生成/图生视频/Minimax参考生视频 高质量 加速版_2086430508090744833.json, 视频生成/图生视频/minimax h3多图参考视频工作流（int8底模+8步提速方案）_2087813787285020674.json, 视频生成/图生视频/海螺H3-全自动图生视频-自动撰写提示词_2086431051328614402.json, 视频生成/文生视频/多参生视频-MiniMax_h3_r2v-视频音频图片参考-智能提示词_2084694636374872065.json, 视频生成/文生视频/智能提示词-多参生视频-MiniMax_h3_r2v-视频音频图片参考_2084262166823268354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_23

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/MiniMax-H3 文生图片+全节点注释_2085181492325601281.json、图片生成/文生图/MiniMaxH3 文生图文生图文生图文生图不是视频！2K加速版_2088278482991280130.json、图片生成/文生图/MiniMaxH3 文生图！2K加速版！_2085238969377316866.json、图片生成/文生图/MiniMaxH3开源 文生图文生图文生图 2K加速版_2088565003669557250.json、图片生成/文生图/MiniMaxH3开源 文生图文生图文生图 2K加速版_2090436462390108161.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 14/15 个有
- `PathchSageAttentionKJ` —— 13/15 个有
- `EasyCache` —— 10/15 个有
- `MiniMaxH3ImageToVideo` —— 10/15 个有
- `JjkText` —— 9/15 个有
- `LoadImage` —— 8/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/15 个有
- `SaveImage` —— 8/15 个有
- `ComfyMathExpression` —— 7/15 个有
- `CreateVideo` —— 7/15 个有
- `ImageFromBatch` —— 7/15 个有
- `PrimitiveFloat` —— 7/15 个有
- `SaveVideo` —— 7/15 个有
- `VAEDecodeAudio` —— 7/15 个有
- `MiniMaxH3ReferenceToVideo` —— 5/15 个有
- `PrimitiveStringMultiline` —— 5/15 个有
- `AudioCrop` —— 3/15 个有
- `LoadAudio` —— 3/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `easy showAnything` —— 3/15 个有
- `孤海注释` —— 3/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `LoadVideo` —— 2/15 个有
- `LoraLoaderModelOnly` —— 2/15 个有
- `MiniMaxH3BlockCacheT8` —— 2/15 个有
- `VHS_LoadVideo` —— 2/15 个有
- `easy anythingIndexSwitch` —— 2/15 个有
- `Label (rgthree)` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
