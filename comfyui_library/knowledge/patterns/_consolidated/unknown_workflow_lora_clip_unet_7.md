---
name: unknown_workflow_lora_clip_unet_7
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.961111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json, 视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json, 视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json, 视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json, 视频生成/文生视频/【加速版】Wan2.2 文生视频_1950372812230934530.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json, 视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json, 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json、视频生成/文生视频/Wan2.2+WAN2.1-lightx2v文生视频_1949895198085136386.json、视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json、视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json、视频生成/文生视频/【加速版】Wan2.2 文生视频_1950372812230934530.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 8/9 个有
- `KSamplerAdvanced` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `Text` —— 4/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `ImpactInt` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `KSampler` —— 1/9 个有
- `WanMoeKSampler` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 9 | 35% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 33% |
| 调度器 | euler | - | 9 | 56% |
| 重绘幅度 | simple | - | 9 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，9 个样本，取值分散，一致性仅 35%
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，9 个样本，一致性 56%
- 重绘幅度 最常用 simple，9 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
