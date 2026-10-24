---
name: unknown_workflow_sampler_unet_vae_88
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.836273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json, 视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json, 视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json, 视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json, 视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）_2084269573662142465.json, 视频生成/图生视频/minMax H3 多参考生视频+加速_2090270612068585473.json, 视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json, 视频生成/文生视频/MINIMAX-H3 多参工作流_2084509251074093057.json, 视频生成/文生视频/MiniMaxH3地表最强阿里3步加速Lora 全能参考速度起飞_2099733663037607937.json, 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_88

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json、视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json、视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json、视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json、视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
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
- `PrimitiveFloat` —— 10/11 个有
- `LoadAudio` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `ComfyMathExpression` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `CreateVideo` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `VHS_LoadVideo` —— 5/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `Int` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `EasyCache` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `PainterVRAM` —— 2/11 个有
- `RTXVideoSuperResolution` —— 2/11 个有
- `SpectrumApplyMiniMaxH3` —— 2/11 个有
- `LTX_lora_loader` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `ModelPreviewOverrideKJ` —— 1/11 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
