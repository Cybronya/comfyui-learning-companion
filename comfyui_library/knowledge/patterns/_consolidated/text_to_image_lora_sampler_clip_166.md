---
name: text_to_image_lora_sampler_clip_166
type: Text To Image
frequency: 10
level: strong
coverage: 0.8583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/H3提示词增强器Qwen3.8本地版 提示词优化视频生成_2108652876636704769.json, 图片生成/反推提示词/MiniMax H3标准格式提示词一键快速生成处理工具_2101716520534630401.json, 图片生成/反推提示词/Qwen3.8提示词增强器｜MiniMax H3反推优化工作流_2097828819615965186.json, 图片生成/反推提示词/gemini-3.5图像反推｜提示词自动生成直出_2090921386087903233.json, 图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json, 图片生成/反推提示词/本地Qwen3.8提示词增强器｜H3反推提示词一键优化_2096276030314074114.json, 图片生成/图生图/MiniMax H3提示词增强器｜Qwen3.8-27B智能优化_2096315918623272961.json, 图片生成/图生图/提示词自动升级｜Qwen3.8-27B为MiniMax H3赋能_2096532589971591169.json, 数字人/数字人/H3提示词增强器 提示词优化智能扩展工具_2099927948383055874.json, 数字人/数字人/声音模型训练翻唱神器 全曲翻唱音频生成处理工具_2113371670797971458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/H3提示词增强器Qwen3.8本地版 提示词优化视频生成_2108652876636704769.json、图片生成/反推提示词/MiniMax H3标准格式提示词一键快速生成处理工具_2101716520534630401.json、图片生成/反推提示词/Qwen3.8提示词增强器｜MiniMax H3反推优化工作流_2097828819615965186.json、图片生成/反推提示词/gemini-3.5图像反推｜提示词自动生成直出_2090921386087903233.json、图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `MiniMaxH3PromptEnhancerT8` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `easy saveText` —— 6/10 个有
- `CR Prompt Text` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `RH_Translator` —— 4/10 个有
- `ShellAgentPluginOutputText` —— 2/10 个有
- `CM_FloatToInt` —— 1/10 个有
- `HAIGC_LoadImagesFromZip` —— 1/10 个有
- `RH_Captioner_Pro` —— 1/10 个有
- `RunningHubRVCOneClickTrain` —— 1/10 个有
- `easy imageSave` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
