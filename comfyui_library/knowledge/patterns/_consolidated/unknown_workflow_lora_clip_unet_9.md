---
name: unknown_workflow_lora_clip_unet_9
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.962667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json, 视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json, 视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json, 视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json, 视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json, 视频生成/文生视频/【加速版】Wan2.2 文生视频_1950372812230934530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json、视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json、视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json、视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json、视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `Text` —— 3/6 个有
- `ImpactInt` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `CFGZeroStar` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `WanVideoNAG` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 50% |
| Prompt 约束强度(CFG) | 8.5 | 4 - 20 | 6 | 42% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 39% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8.5，观测区间 4 - 20，6 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
