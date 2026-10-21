---
name: unknown_workflow_video_sampler_clip_46
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.978727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json, 视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json, 视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json, 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json, 视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json, 视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json, 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json, 视频生成/文生视频/1950151381917327361.json, 视频生成/文生视频/文生视频Holocine电影分镜工作流（自己测试吧）_1985283263507873793.json, 视频生成/文生视频/电影分镜创作test_1982334497687519233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json、视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json、视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json、视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 9/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `INTConstant` —— 3/11 个有
- `Int` —— 2/11 个有
- `ModelPatchTorchSettings` —— 2/11 个有
- `CFGZeroStarAndInit` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `MuyeMathCalculator` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 64% |
| Prompt 约束强度(CFG) | 12 | 6 - 20 | 11 | 50% |
| 采样算法 | 1 | 1 - 3.5 | 11 | 42% |
| 调度器 | euler | - | 11 | 91% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 20，11 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 42%
- 调度器 最常用 euler，11 个样本，一致性 91%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
