---
name: unknown_workflow_video_lora_clip_5
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.938
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/video_wan2_2_14B_灯光工作流+提示词_1950503507558387713.json, 视频生成/文生视频/wan2.2+2.1文生视频_1950156709198217218.json, 视频生成/文生视频/wan2.2官方修改版 2分钟出视频文生视频工作流_1950151381917327361.json, 视频生成/文生视频/wan2.2工作流_2034980882162917377.json, 视频生成/文生视频/wan2.2文生视频-官方极速版_1950456441427693570.json, 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json, 视频生成/文生视频/wan2_2_t2v-生万物+妙转换+广告创意动画-高质量_1973586939590873089.json, 视频生成/文生视频/【最接近官方】Lightx2v-T2V-4步快速文生视频_1972827331947614209.json, 视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json, 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_5

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/video_wan2_2_14B_灯光工作流+提示词_1950503507558387713.json、视频生成/文生视频/wan2.2+2.1文生视频_1950156709198217218.json、视频生成/文生视频/wan2.2官方修改版 2分钟出视频文生视频工作流_1950151381917327361.json、视频生成/文生视频/wan2.2工作流_2034980882162917377.json、视频生成/文生视频/wan2.2文生视频-官方极速版_1950456441427693570.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 9/10 个有
- `PathchSageAttentionKJ` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `easy seed` —— 3/10 个有
- `CFGZeroStar` —— 2/10 个有
- `LayerUtility: PurgeVRAM` —— 2/10 个有
- `Text` —— 2/10 个有
- `UnetLoaderGGUF` —— 2/10 个有
- `WanVideoNAG` —— 2/10 个有
- `CFGZeroStarAndInit` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `WanMoeKSampler` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 50% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 10 | 45% |
| 采样算法 | 1 | 1 - 3.5 | 10 | 40% |
| 调度器 | euler | - | 10 | 50% |
| 重绘幅度 | simple | - | 10 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，10 个样本，取值分散，一致性仅 45%
- 采样算法 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，10 个样本，一致性 50%
- 重绘幅度 最常用 simple，10 个样本，一致性 90%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
