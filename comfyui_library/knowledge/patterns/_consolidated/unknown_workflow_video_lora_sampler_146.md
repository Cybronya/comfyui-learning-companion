---
name: unknown_workflow_video_lora_sampler_146
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.495833
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_replace_2064232122084319234.json, 视频生成/图生视频/video_wan2_2_with_skill_prompt_2013644132241121282.json, 视频生成/图生视频/图片自动出视频_1989490434684669953.json, 视频生成/图生视频/图生视频千问反推版3_1986291016309362690.json, 视频生成/文生视频/Supermate 推荐Qwen3vl视频反推提示+Video_wan2_2_14B视频生成_1982073877964693505.json, 视频生成/文生视频/video_wan2_2_bernini_i2i_2064270918700060673.json, 视频生成/文生视频/video_wan2_2_bernini_multi_r2v_2064268091416207362.json, 视频生成/文生视频/video_wan2_2_bernini_r2v_2064265816681570306.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_changebg_2064251615900688385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json、视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json、视频生成/图生视频/video_wan2_2_bernini_rv2v_replace_2064232122084319234.json、视频生成/图生视频/video_wan2_2_with_skill_prompt_2013644132241121282.json、视频生成/图生视频/图片自动出视频_1989490434684669953.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `CLIPVisionLoader` —— 10/12 个有
- `INTConstant` —— 10/12 个有
- `ImageResizeKJv2` —— 9/12 个有
- `VHS_LoadVideo` —— 8/12 个有
- `BatchImagesNode` —— 7/12 个有
- `BerniniConditioning` —— 7/12 个有
- `AILab_QwenVL` —— 4/12 个有
- `PreviewAny` —— 4/12 个有
- `CLIPVisionEncode` —— 3/12 个有
- `WanImageToVideo` —— 3/12 个有
- `EmptyHunyuanLatentVideo` —— 2/12 个有
- `FlashVSRNode` —— 2/12 个有
- `GetImageRangeFromBatch` —— 2/12 个有
- `GetImageSizeAndCount` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `SaveImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 58% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 12 | 88% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | lcm | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 58%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，12 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
