---
name: unknown_workflow_video_clip_unet_9
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.941556
common_nodes: [CLIPLoader, CLIPTextEncode, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: [easy int]
members: [视频生成/文生视频/1975738907180576770.json, 视频生成/文生视频/1949875905322729473.json, 视频生成/文生视频/1949880459313463297.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json, 视频生成/文生视频/1950654567312740354.json, 视频生成/文生视频/1936054594244087809.json, 视频生成/文生视频/ComfyUI官方图生视频工作流搭建_2050410359365881858.json, 视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/1975738907180576770.json、视频生成/文生视频/1949875905322729473.json、视频生成/文生视频/1949880459313463297.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `KSamplerAdvanced` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `WanImageToVideo` —— 7/9 个有
- `EmptyHunyuanLatentVideo` —— 6/9 个有
- `KSampler` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `CLIPVisionEncode` —— 1/9 个有
- `CLIPVisionLoader` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 6 | 1 - 14 | 9 | 37% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | euler | - | 9 | 78% |
| 重绘幅度 | simple | - | 9 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 14，9 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，9 个样本，一致性 78%
- 重绘幅度 最常用 simple，9 个样本，一致性 78%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy int
