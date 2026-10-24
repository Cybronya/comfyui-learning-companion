---
name: unknown_workflow_sampler_unet_vae_9
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.855304
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json, 图片生成/图生图/千问_2104563424893161474.json, 图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json, 图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json, 图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json, 图片生成/图生图/千问工作流_2102311506384867330.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105647767073935362.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2104737905183903746.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105235774793928705.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105274061088706562.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json, 图片生成/图生图/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102936104516280321.json, 图片生成/图生图/模特换装 Model Outfit Changes Qwen+Image+2.1+图片换装_2105094118673309698.json, 图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json, 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json, 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json, 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json、图片生成/图生图/千问_2104563424893161474.json、图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json、图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json、图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 22/23 个有
- `EmptyLatentImage` —— 22/23 个有
- `QwenImage21Cache` —— 22/23 个有
- `ResolutionSelector` —— 19/23 个有
- `TextGenerateLTX2Prompt` —— 15/23 个有
- `BatchImagesNode` —— 13/23 个有
- `JjkText` —— 12/23 个有
- `CR Text` —— 9/23 个有
- `easy imageConcat` —— 4/23 个有
- `孤海注释` —— 4/23 个有
- `EmptyImage` —— 3/23 个有
- `Note Plus (mtb)` —— 3/23 个有
- `PreviewImage` —— 3/23 个有
- `Anything Everywhere3` —— 1/23 个有
- `CR Prompt Text` —— 1/23 个有
- `PreviewAny` —— 1/23 个有
- `Text Multiline` —— 1/23 个有
- `TextCombinerSix` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 20 - 50 | 23 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 23 | 71% |
| 采样算法 | euler | - | 23 | 96% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 22 | 100% |
| 高度 | 1024 | 1024 - 1624 | 22 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 20 - 50，23 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，23 个样本
- 采样算法 最常用 euler，23 个样本，一致性 96%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，22 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1624，22 个样本，取值集中（一致性 88%）
