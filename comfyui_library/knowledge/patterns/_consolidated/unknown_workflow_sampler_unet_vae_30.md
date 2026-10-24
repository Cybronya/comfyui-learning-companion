---
name: unknown_workflow_sampler_unet_vae_30
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.798235
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax 4步极速版无缝循环动态壁纸_2085615593344036866.json, 视频生成/图生视频/MiniMax H3 ComfyUI单图参考模板工作流（官方模板）_2084663488521265154.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088003246421004290.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088050578806099969.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-美杜莎_2088070116331311105.json, 视频生成/图生视频/MiniMax H3 I2V-f comfyorg_2085033775163076609.json, 视频生成/图生视频/MiniMax H3 I2V-f-l comfyorg_2086105138632155137.json, 视频生成/图生视频/MiniMax H3 图生视频 加速版工作流_2084933797195370498.json, 视频生成/图生视频/MiniMax H3 无缝循环动态壁纸二次元风格live2d自动分辨率_2085541606505140226.json, 视频生成/图生视频/MiniMax H3 首尾帧 加速版 视频生成工作流_2084941106655096834.json, 视频生成/图生视频/MiniMax H3 首尾帧生视频_2084510292645601281.json, 视频生成/图生视频/MiniMax+H3+图生视频+加速版工作流_2087098569571524609.json, 视频生成/图生视频/MiniMaxH3加速版工作流图生视频ENGENG_2087088986627067905.json, 视频生成/图生视频/MiniMaxH3视频生成工作流加速版首尾帧ENGENG_2087088340184162306.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2087076628211003394.json, 视频生成/图生视频/Minimax图生视频I2V_2099170083997315073.json, 视频生成/文生视频/Minimax文生视频T2V_2098449873984122882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_30

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax 4步极速版无缝循环动态壁纸_2085615593344036866.json、视频生成/图生视频/MiniMax H3 ComfyUI单图参考模板工作流（官方模板）_2084663488521265154.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088003246421004290.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088050578806099969.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-美杜莎_2088070116331311105.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 16/17 个有
- `ImageScaleToTotalPixels` —— 16/17 个有
- `LoadImage` —— 16/17 个有
- `ResolutionSelector` —— 15/17 个有
- `VAEDecodeAudio` —— 15/17 个有
- `LoraLoaderModelOnly` —— 8/17 个有
- `MiniMaxH3SigmaShift` —— 7/17 个有
- `PathchSageAttentionKJ` —— 7/17 个有
- `ResizeImageMaskNode` —— 4/17 个有
- `GetNode` —— 3/17 个有
- `SetNode` —— 3/17 个有
- `AudioCrop` —— 2/17 个有
- `ComfySwitchNode` —— 2/17 个有
- `ImageFromBatch` —— 2/17 个有
- `LoadAudio` —— 2/17 个有
- `PrimitiveBoolean` —— 2/17 个有
- `PrimitiveInt` —— 2/17 个有
- `ResizeAndPadImage` —— 2/17 个有
- `easy minimaxH3AudioLock` —— 2/17 个有
- `EasyCache` —— 1/17 个有
- `LTXVSeparateAVLatent` —— 1/17 个有
- `LoraLoaderBypassModelOnly` —— 1/17 个有
- `SaveLatent` —— 1/17 个有
- `TextInputNode` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
