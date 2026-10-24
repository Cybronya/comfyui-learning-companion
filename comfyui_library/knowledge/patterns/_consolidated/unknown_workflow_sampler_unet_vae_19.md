---
name: unknown_workflow_sampler_unet_vae_19
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.78225
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2张参考图_2110029532303552514.json, 视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json, 视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json, 视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json, 视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json, 视频生成/图生视频/CG迷-MiniMax H3参考生视频工作流_2085601489535455234.json, 视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json, 视频生成/图生视频/LynnReal-Onmi 多参考+首尾帧满血4步加速音视频_2101265947867828226.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json, 视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json, 视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json, 视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json, 视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json, 视频生成/图生视频/MiniMax H3-全能参考一图版_2094433073793421313.json, 视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json, 视频生成/图生视频/Minimax H3 单张参考图生视频标准版_2102224374689517569.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频标准版_2102237236300435457.json, 视频生成/图生视频/MinimaxH3 FastH3 Trim多参考+首尾帧满血8步加速音视频生成_2105942822275866626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2张参考图_2110029532303552514.json、视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json、视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json、视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json、视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 19/20 个有
- `LoraLoaderModelOnly` —— 15/20 个有
- `ComfySwitchNode` —— 14/20 个有
- `PrimitiveBoolean` —— 14/20 个有
- `MiniMaxH3ImageToVideo` —— 13/20 个有
- `PrimitiveInt` —— 13/20 个有
- `ResolutionSelector` —— 13/20 个有
- `PrimitiveStringMultiline` —— 10/20 个有
- `MiniMaxH3ReferenceToVideo` —— 9/20 个有
- `GetImageSize` —— 8/20 个有
- `ImageScaleToTotalPixels` —— 5/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/20 个有
- `CR Text` —— 3/20 个有
- `ImageScale` —— 3/20 个有
- `AnySwitch` —— 2/20 个有
- `Fast Bypasser (rgthree)` —— 2/20 个有
- `PathchSageAttentionKJ` —— 2/20 个有
- `H3AdaLNLoRAFix` —— 1/20 个有
- `LoadImageFromUrl` —— 1/20 个有
- `SDVN Any Show` —— 1/20 个有
- `Text` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
