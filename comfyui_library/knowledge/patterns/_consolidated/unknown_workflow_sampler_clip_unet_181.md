---
name: unknown_workflow_sampler_clip_unet_181
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.922125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json, 视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json, 视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json, 视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json, 视频生成/文生视频/万相wan2.2  14B文生视频官方工作流_1950182276686635009.json, 视频生成/文生视频/文生视频wan2.2最新加速dyno_1972639381158862850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_181

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json、视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json、视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `Int` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `SimpleMath+` —— 2/8 个有
- `CustomAddLabel` —— 1/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 8 | 25% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 33% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，8 个样本，取值分散，一致性仅 25%
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
