---
name: unknown_workflow_video_lora_sampler_229
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.807636
common_nodes: [BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, KSamplerAdvanced, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy imageScaleDownToSize]
problems: []
missing: []
members: [平台全量/Bernini视频编辑_2062053081956831234.json, 平台全量/视频编辑 物体替换，去水印字幕_2088931943772672001.json, 数字人/数字人/视频局部重绘 人物替换，去字幕，风格转换 加速版 Bernini-贝尔尼尼_2062126637579329537.json, 数字人/数字人/视频编辑 物体替换，去水印字幕，风格转换等等多功能 Bernini贝尔尼尼 加速版_2062107326299070466.json, 视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json, 视频生成/图生视频/Bernini贝尔尼尼高噪无加速版（超牛动作迁移）_2062715583887663106.json, 视频生成/图生视频/服装新玩法-Bernini人物替换_2020633781832519681.json, 视频生成/图生视频/服装模特视频背景替换_2065039973153333250.json, 视频生成/图生视频/高噪无加速版_2062714987814146049.json, 视频生成/文生视频/Bernini-R 主体替换视频编辑流程_2062503702258348033.json, 视频生成/文生视频/Bernini-R 参考背景视频替换流程_2062503708742733826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_229

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Bernini视频编辑_2062053081956831234.json、平台全量/视频编辑 物体替换，去水印字幕_2088931943772672001.json、数字人/数字人/视频局部重绘 人物替换，去字幕，风格转换 加速版 Bernini-贝尔尼尼_2062126637579329537.json、数字人/数字人/视频编辑 物体替换，去水印字幕，风格转换等等多功能 Bernini贝尔尼尼 加速版_2062107326299070466.json、视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerAdvanced`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 10/11 个有
- `ImageFromBatch` —— 10/11 个有
- `RHLLMChatNode` —— 7/11 个有
- `Int` —— 6/11 个有
- `SimpleMath+` —— 5/11 个有
- `PrimitiveInt` —— 4/11 个有
- `StringReplace` —— 4/11 个有
- `Text` —— 4/11 个有
- `easy showAnything` —— 4/11 个有
- `image_scale_pixel_v2` —— 4/11 个有
- `JjkText` —— 3/11 个有
- `TextCombinerTwo` —— 3/11 个有
- `CR Text` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 73% |
| Prompt 约束强度(CFG) | 14 | 4 - 14 | 11 | 66% |
| 采样算法 | 1 | 1 - 3 | 11 | 51% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 73%
- Prompt 约束强度(CFG) 中位数 14，观测区间 4 - 14，11 个样本
- 采样算法 中位数 1，观测区间 1 - 3，11 个样本
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
