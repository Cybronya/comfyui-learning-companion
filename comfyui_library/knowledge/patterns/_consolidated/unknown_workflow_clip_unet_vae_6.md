---
name: unknown_workflow_clip_unet_vae_6
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.987
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyHunyuanLatentVideo, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json, 视频生成/文生视频/1949895198085136386.json, 视频生成/文生视频/1950219353737314306.json, 视频生成/文生视频/1950412197002436609.json, 视频生成/文生视频/1956007153972727810.json, 视频生成/文生视频/1949875835437236226.json, 视频生成/文生视频/1950372812230934530.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json、视频生成/文生视频/1949895198085136386.json、视频生成/文生视频/1950219353737314306.json、视频生成/文生视频/1950412197002436609.json、视频生成/文生视频/1956007153972727810.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `SimpleMath+` —— 3/7 个有
- `ImpactInt` —— 2/7 个有
- `Int` —— 2/7 个有
- `Text` —— 2/7 个有
- `KSampler` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 9 | 4 - 20 | 7 | 42% |
| 采样算法 | 2.25 | 1 - 3.5 | 6 | 44% |
| 调度器 | euler | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 9，观测区间 4 - 20，7 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 2.25，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 71%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
