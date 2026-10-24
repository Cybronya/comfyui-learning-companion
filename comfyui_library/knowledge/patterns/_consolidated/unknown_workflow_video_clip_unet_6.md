---
name: unknown_workflow_video_clip_unet_6
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.938455
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.1图生视频_1924384393446477826.json, 视频生成/图生视频/Wan2.1图生视频_1940719231082328066.json, 视频生成/图生视频/Wan2.1图生视频_1985686489952657410.json, 视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json, 视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json, 视频生成/图生视频/Wan2.1首尾帧动画_1925841932033937410.json, 视频生成/图生视频/Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json, 视频生成/图生视频/wan2.2-i2v_官方版图生视频_1967246222643826690.json, 视频生成/图生视频/wan2.2图生视频_2032294659132755970.json, 视频生成/图生视频/wan2.2图生视频首尾帧_2040056903719460866.json, 视频生成/图生视频/通义wan2.1：图生视频（新）_1944367617996148737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.1图生视频_1924384393446477826.json、视频生成/图生视频/Wan2.1图生视频_1940719231082328066.json、视频生成/图生视频/Wan2.1图生视频_1985686489952657410.json、视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json、视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 8/11 个有
- `WanImageToVideo` —— 8/11 个有
- `ModelSamplingSD3` —— 6/11 个有
- `ImageResize+` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `KSamplerAdvanced` —— 3/11 个有
- `WanFirstLastFrameToVideo` —— 3/11 个有
- `ImageResizeKJ` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `GetImageSize+` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 30 | 8 | 64% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 11 | 59% |
| 采样算法 | uni_pc | - | 11 | 45% |
| 调度器 | simple | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，11 个样本
- 采样算法 最常用 uni_pc，11 个样本，一致性 45%
- 调度器 最常用 simple，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
