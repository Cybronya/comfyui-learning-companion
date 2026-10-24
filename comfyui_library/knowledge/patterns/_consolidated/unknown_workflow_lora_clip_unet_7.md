---
name: unknown_workflow_lora_clip_unet_7
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.971
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json, 视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json, 视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json, 视频生成/文生视频/wan2.2-文生视频-KJ加速版-输入大纲-自动优化提示词_1955139127446573057.json, 视频生成/文生视频/wan2.2-文生视频-火焰人_1955297362048684033.json, 视频生成/文生视频/wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json, 视频生成/文生视频/【加速版】Wan2.2 文生视频_1950372812230934530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json、视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json、视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json、视频生成/文生视频/wan2.2-文生视频-KJ加速版-输入大纲-自动优化提示词_1955139127446573057.json、视频生成/文生视频/wan2.2-文生视频-火焰人_1955297362048684033.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `ImpactInt` —— 5/7 个有
- `SimpleMath+` —— 5/7 个有
- `CR Text Replace` —— 3/7 个有
- `RH_Prompter` —— 3/7 个有
- `TextBox` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `Text` —— 2/7 个有
- `KSampler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 10 | 4 - 20 | 7 | 54% |
| 采样算法 | 3.5 | 1 - 3.5 | 6 | 70% |
| 调度器 | euler | - | 7 | 71% |
| 重绘幅度 | simple | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 20，7 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，6 个样本
- 调度器 最常用 euler，7 个样本，一致性 71%
- 重绘幅度 最常用 simple，7 个样本，一致性 71%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
