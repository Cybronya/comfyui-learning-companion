---
name: unknown_workflow_video_lora_sampler_60
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.825947
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速 图生视频 -zip_2086179408511062017.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速+图生视频_2095722417233682433.json, 视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 4步极速版_2090795830067417090.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 8步加速版_2090756411985850369.json, 视频生成/图生视频/1896972443683069953.json, 视频生成/图生视频/MiniMax H3-4步加速-图生视频_2090916306450210818.json, 视频生成/图生视频/MiniMax H3-参考生视频V1-双时钟-8步高质量极速-step600_2086823760027545602.json, 视频生成/图生视频/MiniMax H3-参考生视频V1-双时钟-8步高质量极速-step600_2087059347460411394.json, 视频生成/图生视频/MiniMax H3-参考生视频V1-双时钟-8步高质量极速-step600_2087069140904407041.json, 视频生成/图生视频/MiniMax H3-参考生视频V1-双时钟-8步高质量极速-step600_2087886342087860226.json, 视频生成/图生视频/MiniMax H3-参考生视频V1-双时钟-8步高质量极速_2085708995028938754.json, 视频生成/图生视频/MiniMax H3-图生视频V1-双时钟-8步高质量极速-step600_2086814507325808641.json, 视频生成/图生视频/MiniMax H3-图生视频V1-双时钟-8步高质量极速-step600_2087891422266609666.json, 视频生成/图生视频/MiniMax H3-图生视频V1-双时钟-8步高质量极速_2085709043984855041.json, 视频生成/图生视频/MiniMax H3-首尾帧视频V1-双时钟-8步高质量极速-step600_2087895091745738753.json, 视频生成/图生视频/MiniMax-H3 单图换装工作流_2097684790219726850.json, 视频生成/图生视频/minimax三图工作流_2092594675935956993.json, 视频生成/图生视频/双时钟采样4步无损加速｜MiniMAX-H3-T8图生视频_2096460092848828418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速 图生视频 -zip_2086179408511062017.json、视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速+图生视频_2095722417233682433.json、视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json、视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 4步极速版_2090795830067417090.json、视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 8步加速版_2090756411985850369.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 18/19 个有
- `PrimitiveFloat` —— 18/19 个有
- `MiniMaxH3AVDecodeT8` —— 17/19 个有
- `ResolutionSelector` —— 16/19 个有
- `孤海注释` —— 10/19 个有
- `GetImageSize` —— 3/19 个有
- `ImageScaleToTotalPixels` —— 3/19 个有
- `Int` —— 2/19 个有
- `VAEDecode` —— 2/19 个有
- `VAEDecodeAudio` —— 2/19 个有
- `CM_IntToFloat` —— 1/19 个有
- `Float` —— 1/19 个有
- `GoohaiUniversalSlider` —— 1/19 个有
- `easy int` —— 1/19 个有
- `solarL_SaveImagesToZip` —— 1/19 个有
- `忽略多组孤海` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
