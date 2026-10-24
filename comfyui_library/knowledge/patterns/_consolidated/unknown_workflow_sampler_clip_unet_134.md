---
name: unknown_workflow_sampler_clip_unet_134
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.966111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json, 图片生成/文生图/wan2.2超级加速文生视频_1957777125837303810.json, 视频生成/图生视频/wan2.2 优化2.0 文生视频14B_1950898146819899393.json, 视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json, 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json, 视频生成/文生视频/wan2.2文生视频（kj模型加速版）_1949875835437236226.json, 视频生成/文生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%文生视频工作流_1968491886845546497.json, 视频生成/文生视频/文生视频Holocine电影分镜工作流（自己测试吧）_1985283263507873793.json, 视频生成/文生视频/最新Wan2.2文生视频_1949836969900687362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_134

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json、图片生成/文生图/wan2.2超级加速文生视频_1957777125837303810.json、视频生成/图生视频/wan2.2 优化2.0 文生视频14B_1950898146819899393.json、视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json、视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `Int` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `ModelPatchTorchSettings` —— 4/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `INTConstant` —— 2/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `MuyeMathCalculator` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 67% |
| Prompt 约束强度(CFG) | 9 | 4 - 20 | 9 | 45% |
| 采样算法 | 1 | 1 - 3.5 | 9 | 41% |
| 调度器 | euler | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 9，观测区间 4 - 20，9 个样本，取值分散，一致性仅 45%
- 采样算法 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 41%
- 调度器 最常用 euler，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
