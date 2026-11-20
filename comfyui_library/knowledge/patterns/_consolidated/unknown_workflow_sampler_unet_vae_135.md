---
name: unknown_workflow_sampler_unet_vae_135
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.723667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Minimax H3 人物替换单人版  自动反推_2099803064780812290.json, 图片生成/图生图/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）james001###_2089273278652309506.json, 图片生成/图生图/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）james001###_2089268665731604481.json, 图片生成/文生图/MiniMax H3 FL2VA开源版-人物参考_2084833557930926081.json, 平台全量/trim fast minimax_2108240526796476417.json, 视频生成/图生视频/H3-官方长视频续接_2095155400160141314.json, 视频生成/文生视频/H3-官方长视频_2092501348708343810.json, 视频生成/文生视频/影视级minimax h3，无限长视频接续-手动版_2096601875046027266.json, 视频生成/文生视频/长视频续接+去油+高质量minimax-H3-官方版-无限延长视频-手动版_2092974453855703041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_135

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Minimax H3 人物替换单人版  自动反推_2099803064780812290.json、图片生成/图生图/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）james001###_2089273278652309506.json、图片生成/图生图/lightx2v 300%加速 MinimaxH3-文生+图生视频（支持首尾帧）james001###_2089268665731604481.json、图片生成/文生图/MiniMax H3 FL2VA开源版-人物参考_2084833557930926081.json、平台全量/trim fast minimax_2108240526796476417.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `LoadAudio` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `ExtendIntermediateSigmas` —— 5/9 个有
- `GetImageRangeFromBatch` —— 5/9 个有
- `ImageAddNoise` —— 5/9 个有
- `MiniMaxH3AddGuide` —— 5/9 个有
- `ModelPreviewOverrideKJ` —— 5/9 个有
- `PrimitiveBoolean` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `TrimAudioDuration` —— 3/9 个有
- `GetNode` —— 2/9 个有
- `JjkText` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `忽略多组孤海` —— 2/9 个有
- `Bjornulf_ShowFloat` —— 1/9 个有
- `JoinStrings` —— 1/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有
- `VHS_VideoInfoLoaded` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
