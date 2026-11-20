---
name: unknown_workflow_sampler_unet_vae_143
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.836333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json, 视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json, 视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json, 视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json, 视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）_2084269573662142465.json, 视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json, 视频生成/图生视频/minimax h3多图参考视频工作流（int8底模+8步提速方案）_2087813787285020674.json, 视频生成/文生视频/Minimax-H3 (电影质感_8步加速版)_2093740212219367425.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_143

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json、视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json、视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json、视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json、视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `LoadAudio` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `Int` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `EasyCache` —— 2/9 个有
- `PainterVRAM` —— 2/9 个有
- `AudioCrop` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `MiniMaxH3AddGuide` —— 1/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
