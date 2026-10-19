---
name: unknown_workflow_sampler_unet_vae_20
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.815706
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json, 视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json, 视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json, 视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2107413322575470593.json, 视频生成/图生视频/FastVideo-FastH3-8-Step-V2 图生视频_2101581826061062145.json, 视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json, 视频生成/图生视频/MiniMax H3 4步 首尾帧图生视频_2090639499977117697.json, 视频生成/图生视频/MiniMax H3 4步 首帧图生视频_2090629891019599874.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json, 视频生成/图生视频/MiniMax H3：参考生视频（加速）_2096113080844513282.json, 视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json, 视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2109867240077217794.json, 视频生成/图生视频/R2V-参考生视频-5060Ti16G-极速加速版_2102730812373422081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_20

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json、视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json、视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json、视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json、视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 15/17 个有
- `LoraLoaderModelOnly` —— 12/17 个有
- `GetImageSize` —— 10/17 个有
- `ImageScaleToTotalPixels` —— 9/17 个有
- `PrimitiveInt` —— 9/17 个有
- `ResolutionSelector` —— 9/17 个有
- `ComfySwitchNode` —— 7/17 个有
- `MiniMaxH3SigmaShift` —— 7/17 个有
- `PrimitiveBoolean` —— 7/17 个有
- `ModelAttentionBackend` —— 6/17 个有
- `CR Text` —— 5/17 个有
- `BlockSparseAttention` —— 4/17 个有
- `PrimitiveStringMultiline` —— 4/17 个有
- `ImageScale` —— 3/17 个有
- `MiniMaxH3ReferenceToVideo` —— 3/17 个有
- `LoadAudio` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `MiniMaxH3ContextIR` —— 1/17 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/17 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 1/17 个有
- `ShowText|pysssss` —— 1/17 个有
- `Text` —— 1/17 个有
- `XB_ReferenceAny` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
