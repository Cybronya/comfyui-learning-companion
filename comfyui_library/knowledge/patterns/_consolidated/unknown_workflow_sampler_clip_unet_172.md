---
name: unknown_workflow_sampler_clip_unet_172
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.953875
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json, 视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json, 视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json, 视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json, 视频生成/文生视频/【阡陌】wan2.2 GGUF+light4步加速lora文生视频工作流_1967793949974867969.json, 视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_172

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json、视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json、视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json、视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json、视频生成/文生视频/【阡陌】wan2.2 GGUF+light4步加速lora文生视频工作流_1967793949974867969.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `Int` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `SimpleMath+` —— 2/8 个有
- `CustomAddLabel` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 8 | 16% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 37% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 16%
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
