---
name: unknown_workflow_sampler_unet_vae_109
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.867182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json, 视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json, 视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json, 视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json, 视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2099770316435316738.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2100031727967232001.json, 视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_109

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json、视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json、视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json、视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json、视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `PrimitiveFloat` —— 8/11 个有
- `ResolutionSelector` —— 8/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `LoadImage` —— 6/11 个有
- `Label (rgthree)` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `easy int` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `Seed (rgthree)` —— 2/11 个有
- `ImageScale` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `YK_LoadImageFromURL` —— 1/11 个有
- `easy positive` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
