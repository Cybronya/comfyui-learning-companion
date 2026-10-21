---
name: unknown_workflow_sampler_unet_vae_51
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.791182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json, 视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json, 视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2084892402388652033.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086998199218294786.json, 视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json, 视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json, 视频生成/图生视频/MinimaxH3 ref2va全能多参工作流_2084512370860318722.json, 视频生成/图生视频/MinimaxH3视频人物替换_2095672328909836290.json, 视频生成/图生视频/MinimaxH3视频人物替换_2109569066229919746.json, 视频生成/图生视频/雷霆运镜Minimax H3 最强视频参考，动作迁移，人物替换_2090101579029504002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json、视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json、视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json、视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2084892402388652033.json、视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086998199218294786.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `MiniMaxH3ReferenceToVideo` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `ResolutionSelector` —— 8/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `VHS_VideoCombine` —— 5/11 个有
- `LoadAudio` —— 4/11 个有
- `PrimitiveInt` —— 4/11 个有
- `VHS_VideoInfo` —— 4/11 个有
- `GetImageSize` —— 3/11 个有
- `ImageConcanate` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `EasyCache` —— 2/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `PainterVRAM` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
