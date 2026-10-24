---
name: unknown_workflow_upscale_latent_upscale_sampler_8
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.882091
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Characters Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+H3+_2104367488405434370.json, 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107279313535062017.json, 视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json, 视频生成/图生视频/H3 角色替换_2085882691152605185.json, 视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json, 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107331983230717954.json, 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json, 视频生成/图生视频/People+Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+H3+_2110176278711193602.json, 视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json, 视频生成/图生视频/h3双采样高清流_2092571899955081218.json, 视频生成/视频生视频/Minimax+H3+多参角色替换Lora，二采放大_2106244704005345281.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Characters Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+H3+_2104367488405434370.json、视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107279313535062017.json、视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json、视频生成/图生视频/H3 角色替换_2085882691152605185.json、视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 10/11 个有
- `VHS_VideoCombine` —— 10/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `ManualSigmas` —— 8/11 个有
- `ModelPreviewOverrideKJ` —— 8/11 个有
- `CR Prompt Text` —— 6/11 个有
- `RHHiddenNodes` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `VHS_LoadVideo` —— 3/11 个有
- `CreateVideo` —— 2/11 个有
- `EmptyImage` —— 2/11 个有
- `FlashVSRNode` —— 2/11 个有
- `H3SigmaRefiner` —— 2/11 个有
- `MiniMaxLowVRAMAttention` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `Sleep` —— 2/11 个有
- `Text` —— 2/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `Lora Loader Stack (rgthree)` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `easy float` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
