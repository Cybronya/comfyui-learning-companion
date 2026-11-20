---
name: unknown_workflow_sampler_unet_vae_216
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.889143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json, 视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json, 视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json, 视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json, 视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json, 视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json, 视频生成/文生视频/文生视频-MiniMaxH3-BV1-模板_2090725747148288002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_216

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json、视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json、视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json、视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json、视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
