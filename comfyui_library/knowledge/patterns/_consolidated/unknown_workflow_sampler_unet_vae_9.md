---
name: unknown_workflow_sampler_unet_vae_9
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.729
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json, 视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json, 视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json, 视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json, 视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json, 视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json, 视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json, 视频生成/图生视频/MiniMax H3-全能参考一图版_2094433073793421313.json, 视频生成/图生视频/MiniMax H3全能参考（图片、音频、视频皆可参考）_2084166446040567809.json, 视频生成/图生视频/MiniMax H3：参考生视频_2095783894242127874.json, 视频生成/图生视频/MiniMax H3：参考生视频（加速）_2096113080844513282.json, 视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json, 视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2109867240077217794.json, 视频生成/图生视频/MiniMax_H3_七套服装连续换装_2094786595428847617.json, 视频生成/图生视频/Minimax H3 单张参考图生视频标准版_2102224374689517569.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频标准版_2102237236300435457.json, 视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json, 视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json, 视频生成/图生视频/Minimax图生视频I2V_2099170083997315073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json、视频生成/图生视频/MiniMax H3 图生视频（开源版）_2084993401539358721.json、视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 19/21 个有
- `ComfySwitchNode` —— 18/21 个有
- `PrimitiveBoolean` —— 18/21 个有
- `PrimitiveInt` —— 18/21 个有
- `ResolutionSelector` —— 14/21 个有
- `MiniMaxH3ImageToVideo` —— 12/21 个有
- `PrimitiveStringMultiline` —— 11/21 个有
- `MiniMaxH3ReferenceToVideo` —— 10/21 个有
- `GetImageSize` —— 9/21 个有
- `ImageScaleToTotalPixels` —— 6/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/21 个有
- `LoadAudio` —— 4/21 个有
- `CR Text` —— 3/21 个有
- `ImageScale` —— 3/21 个有
- `EmptyImage` —— 2/21 个有
- `MiniMaxH3SigmaShift` —— 2/21 个有
- `PreviewImage` —— 2/21 个有
- `AudioCrop` —— 1/21 个有
- `BlockSparseAttention` —— 1/21 个有
- `GetNode` —— 1/21 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 1/21 个有
- `ModelAttentionBackend` —— 1/21 个有
- `SetNode` —— 1/21 个有
- `VHS_LoadVideo` —— 1/21 个有
- `easy minimaxH3AudioLock` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
