---
key: 图片生成/反推提示词/图片转提示词技术对比，JoyCaption，Florence，Tagger，CLIP，Janus_1896557847901872129.json
name: 图片转提示词技术对比，JoyCaption，Florence，Tagger，CLIP，Janus_1896557847901872129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/图片转提示词技术对比，JoyCaption，Florence，Tagger，CLIP，Janus_1896557847901872129.json
hash: e37a8d9d4080eadb
coverage: 0.69697
learned_at: 2026-10-26 01:47:58
nodes: [Fast Groups Muter (rgthree), Bjornulf_ShowStringText, ShellAgentPluginOutputText, LayerUtility: JoyCaption2, GetNode, Bjornulf_ShowStringText, GetNode, ClipInterrogator, WD14Tagger|pysssss, Bjornulf_ShowStringText, Bjornulf_ShowStringText, Note Plus (mtb), Bjornulf_ShowStringText, GetNode, RH_Captioner, GetNode, Bjornulf_ShowStringText, Bjornulf_ShowStringText, GetNode, GetNode, LayerUtility: LoadVQAModel, GetNode, JanusModelLoader, JanusImageUnderstanding, LayerUtility: VQAPrompt, LoadImage, SetNode, LayerMask: LoadFlorence2Model, GetNode, LayerUtility: Florence2Image2Prompt, SaveImage, LayerUtility: QWenImage2Prompt, Bjornulf_ShowStringText]
patterns: []
missing: []
---

# 图片生成/反推提示词/图片转提示词技术对比，JoyCaption，Florence，Tagger，CLIP，Janus_1896557847901872129.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/图片转提示词技术对比，JoyCaption，Florence，Tagger，CLIP，Janus_1896557847901872129.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（33 个）：
- `Fast Groups Muter (rgthree)`
- `Bjornulf_ShowStringText`
- `ShellAgentPluginOutputText`
- `LayerUtility: JoyCaption2`
- `GetNode`
- `Bjornulf_ShowStringText`
- `GetNode`
- `ClipInterrogator`
- `WD14Tagger|pysssss`
- `Bjornulf_ShowStringText`
- `Bjornulf_ShowStringText`
- `Note Plus (mtb)`
- `Bjornulf_ShowStringText`
- `GetNode`
- `RH_Captioner`
- `GetNode`
- `Bjornulf_ShowStringText`
- `Bjornulf_ShowStringText`
- `GetNode`
- `GetNode`
- `LayerUtility: LoadVQAModel`
- `GetNode`
- `JanusModelLoader`
- `JanusImageUnderstanding`
- `LayerUtility: VQAPrompt`
- `LoadImage`
- `SetNode`
- `LayerMask: LoadFlorence2Model`
- `GetNode`
- `LayerUtility: Florence2Image2Prompt`
- `SaveImage`
- `LayerUtility: QWenImage2Prompt`
- `Bjornulf_ShowStringText`

## 知识

覆盖率 **70%**（23/33）

**有卡**：`Bjornulf_ShowStringText`、`ShellAgentPluginOutputText`、`LayerUtility: JoyCaption2`、`ClipInterrogator`、`WD14Tagger|pysssss`、`Note Plus (mtb)`、`RH_Captioner`、`LayerUtility: LoadVQAModel`、`JanusModelLoader`、`JanusImageUnderstanding`、`LayerUtility: VQAPrompt`、`LoadImage`、`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`SaveImage`、`LayerUtility: QWenImage2Prompt`

**用到的条目**：SaveImage、LoadImage、ClipInterrogator、LayerUtility: Florence2Image2Prompt、LayerUtility: QWenImage2Prompt、LayerUtility: VQAPrompt、ShellAgentPluginOutputText、RH_Captioner
