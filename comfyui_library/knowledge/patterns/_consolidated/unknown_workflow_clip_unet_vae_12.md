---
name: unknown_workflow_clip_unet_vae_12
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.967286
common_nodes: [CLIPLoader, CLIPTextEncode, SaveAnimatedWEBP, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/image_to_video_wan22_14B官方优化版_1950499114352103426.json, 视频生成/图生视频/【AI由北】Wan2.1 图生视频 全能版本_1928340598107815937.json, 视频生成/图生视频/【Wan2.1图生视频】小红书抖音_美女爆款视频生成_1904560347657777154.json, 视频生成/文生视频/text_to_video_wan22_14B官方优化版_1950503480169517058.json, 视频生成/文生视频/【AI由北】Wan2.1 文生视频 全能版_1927645156290215937.json, 视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json, 视频生成/文生视频/通义万相WAN2.1文生视频基础工作流_1924310147001143297.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/image_to_video_wan22_14B官方优化版_1950499114352103426.json、视频生成/图生视频/【AI由北】Wan2.1 图生视频 全能版本_1928340598107815937.json、视频生成/图生视频/【Wan2.1图生视频】小红书抖音_美女爆款视频生成_1904560347657777154.json、视频生成/文生视频/text_to_video_wan22_14B官方优化版_1950503480169517058.json、视频生成/文生视频/【AI由北】Wan2.1 文生视频 全能版_1927645156290215937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `SaveAnimatedWEBP`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveWEBM` —— 6/7 个有
- `KSampler` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `ModelSamplingSD3` —— 4/7 个有
- `WanImageToVideo` —— 4/7 个有
- `CLIPVisionEncode` —— 3/7 个有
- `CLIPVisionLoader` —— 3/7 个有
- `EmptyHunyuanLatentVideo` —— 3/7 个有
- `KSamplerAdvanced` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 80% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 7 | 37% |
| 采样算法 | uni_pc | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，7 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 uni_pc，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
